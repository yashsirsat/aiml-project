HOMEVALUE — HOUSE PRICE PREDICTION (AIML COLLEGE PROJECT)

EASY WINDOWS SETUP
1. Install Python 3.11 or 3.12 from https://www.python.org/downloads/ if needed.
2. During installation, tick "Add Python to PATH".
3. Extract this ZIP into a normal folder, for example on your Desktop.
4. Double-click START_WEBSITE.bat.
5. The first run needs an internet connection to install Python libraries and may take a few minutes.
6. When the terminal says the server is running, open http://127.0.0.1:5000 in Chrome or Edge.
7. Keep the terminal window open while using the site. Press Ctrl+C in the terminal to stop it.

FILES
app.py                  Flask backend, data loading, model training and prediction
templates/index.html    Frontend HTML
static/style.css        Website styling
house_prices.csv        600 illustrative sample property records
requirements.txt        Required Python libraries
START_WEBSITE.bat       Double-click launcher for Windows
PROJECT_REPORT.md       Report explanation and viva questions

FEATURES
- Inputs: area (sq ft), city, bedrooms, bathrooms and property age
- Output: predicted price in Indian rupees, lakhs and crores
- Algorithm: Random Forest Regression
- Evaluation: held-out test MAE and R-squared are computed at startup
- Included cities: Pune, Mumbai, Bengaluru, Hyderabad, Delhi, Chennai, Nagpur, Nashik, Jaipur, Indore, Ahmedabad and Lucknow

IMPORTANT
The included dataset is synthetic and created for educational demonstration. Predictions and metrics are illustrative, not real property market valuations. Replace the sample data with reliable, licensed real property transaction data before making real-world decisions.

TROUBLESHOOTING
- "Python was not found": install Python and enable Add Python to PATH.
- Installation fails: check internet access and run START_WEBSITE.bat again.
- Browser cannot connect: ensure the black terminal window is still open and use exactly http://127.0.0.1:5000.
