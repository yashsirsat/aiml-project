from pathlib import Path
import pandas as pd
from flask import Flask, render_template, request
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)
NUMERIC = ["area_sqft", "bedrooms", "bathrooms", "age_years"]
CATEGORICAL = ["location"]
FEATURES = NUMERIC + CATEGORICAL

def train_model():
    data = pd.read_csv(BASE_DIR / "house_prices.csv")
    X, y = data[FEATURES], data["price_lakh"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    prep = ColumnTransformer([
        ("numeric", "passthrough", NUMERIC),
        ("location", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL)
    ])
    model = Pipeline([
        ("preprocessor", prep),
        ("regressor", RandomForestRegressor(n_estimators=120, random_state=42, min_samples_leaf=2))
    ])
    model.fit(X_train, y_train)
    test_predictions = model.predict(X_test)
    metrics = {"mae": round(float(mean_absolute_error(y_test, test_predictions)), 2),
               "r2": round(float(r2_score(y_test, test_predictions)), 3), "rows": len(data)}
    model.fit(X, y)
    return model, metrics, sorted(data.location.unique().tolist())

model, metrics, locations = train_model()

@app.route("/", methods=["GET", "POST"])
def index():
    defaults = {"area_sqft":"1000", "location":"Pune", "bedrooms":"2", "bathrooms":"2", "age_years":"5"}
    form = defaults.copy()
    prediction = error = None
    if request.method == "POST":
        form = {k: request.form.get(k, "").strip() for k in defaults}
        try:
            area, beds, baths, age = float(form["area_sqft"]), int(form["bedrooms"]), int(form["bathrooms"]), int(form["age_years"])
            city = form["location"]
            if not 200 <= area <= 10000: raise ValueError("Area must be between 200 and 10,000 square feet.")
            if not 1 <= beds <= 10: raise ValueError("Bedrooms must be between 1 and 10.")
            if not 1 <= baths <= 10: raise ValueError("Bathrooms must be between 1 and 10.")
            if not 0 <= age <= 100: raise ValueError("Property age must be between 0 and 100 years.")
            if city not in locations: raise ValueError("Please choose a location from the list.")
            row = pd.DataFrame([{"area_sqft":area, "bedrooms":beds, "bathrooms":baths, "age_years":age, "location":city}])
            lakh = max(0.0, float(model.predict(row)[0]))
            prediction = {"formatted":f"₹{lakh:,.2f} lakh", "crore":f"₹{lakh/100:,.2f} crore"}
        except (ValueError, TypeError) as exc:
            error = str(exc) or "Please enter valid property details."
    return render_template("index.html", form=form, prediction=prediction, error=error, locations=locations, metrics=metrics)

@app.route("/health")
def health():
    return {"status":"ok", "model":"RandomForestRegressor"}

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
