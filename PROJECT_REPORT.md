# HomeValue: House Price Prediction Using Machine Learning

## Abstract
HomeValue is a beginner-friendly web application that estimates residential property prices from area, location, bedrooms, bathrooms, and property age. It uses Python, Flask, pandas, and Random Forest Regression to demonstrate a full machine-learning workflow.

## Problem Statement
Estimating property prices manually is difficult because multiple factors influence value. This project demonstrates how a regression model can learn patterns from example records and estimate a value from user-entered features.

## Objectives
- Create a simple frontend for entering property details.
- Load and preprocess property data.
- Train a supervised regression model.
- Evaluate it with MAE and R-squared on a held-out test set.
- Connect the model to a Flask backend and display predictions.

## Technologies
Python 3, Flask, pandas, scikit-learn, HTML, CSS.

## Features and Target
Inputs: area in square feet, city/location, bedroom count, bathroom count, property age in years. Target: price in Indian rupees lakhs.

## Methodology
1. Load `house_prices.csv`.
2. Separate features and target.
3. Split records into 80% training and 20% test sets.
4. Pass numeric features through and one-hot encode city.
5. Train a RandomForestRegressor.
6. Calculate MAE and R-squared on the test split.
7. Fit the final model on all available rows.
8. Use Flask to validate form input and show the predicted value.

## Algorithm
Random Forest Regression is an ensemble method that combines predictions from multiple decision trees. It can learn non-linear relationships and interactions between features.

## Modules
- Data: reads CSV records.
- Preprocessing: one-hot encodes location.
- Training and evaluation: fits model and calculates metrics.
- Backend: validates user input and generates predictions.
- Frontend: collects property details and displays estimate.

## Evaluation
The app calculates MAE (in lakh units) and R-squared on a held-out test split at startup. These metrics describe performance on the included sample data only.

## Limitations and Ethics
The included 600-row dataset is synthetic and illustrative, not verified real transaction data. The model supports only a limited list of cities and features. Real prices also depend on locality, property type, floor, amenities, legal status, and current market conditions. Do not use the estimate as an official valuation or financial advice.

## Future Scope
Use a reliable real dataset; add property type, furnishing, floor and amenities; compare multiple algorithms; plot feature importance and errors; persist the trained model to reduce startup time.

## Conclusion
The project demonstrates an end-to-end machine-learning application connecting a regression model to a simple user interface.

## Viva Questions
1. What is supervised learning? Learning from examples with known targets.
2. Why is this regression? The output is a continuous numeric value.
3. What is Random Forest? An ensemble of decision trees whose predictions are combined.
4. Why encode location? Models require categorical text to be represented numerically.
5. What is a train/test split? Training on one subset and evaluating on unseen records.
6. What is MAE? Mean absolute difference between actual and predicted values.
7. What is overfitting? Learning training-specific patterns that generalize poorly.
8. Can this be used to buy a house? No; sample data is synthetic and predictions are educational only.
