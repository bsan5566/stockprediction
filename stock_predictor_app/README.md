# 📈 AI-Powered Stock Price Prediction Web App

This is an advanced-level machine learning project for predicting future stock prices using both **LSTM (deep learning)** and **ARIMA (time series analysis)** models. The app is built with **Streamlit** and allows users to upload their own stock CSV files for analysis.

---

## 📜 Features
- Upload CSV files with historical stock data
- Visualize closing price trends
- Predict next 30 days using:
  - LSTM Neural Network
  - ARIMA model
- Download forecasted results as CSV

---

## 📁 Directory Structure
```
stock_predictor_app/
├── app.py
├── utils/
│   ├── preprocessing.py
│   └── prediction.py
├── sample_stock.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation
```bash
# Clone the repository or unzip the project folder
cd stock_predictor_app

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Running the App
```bash
streamlit run app.py
```
Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📄 Sample CSV Format
Your CSV file should contain the following columns:
```
Date, Open, High, Low, Close, Volume
```
Make sure the **Date** column is in `YYYY-MM-DD` format.

---

## ✨ Future Improvements
- Add technical indicators (MACD, RSI, Bollinger Bands)
- Include sentiment analysis from news/Twitter
- Add support for live stock API data

---

## ✉️ Contact
Created by **Santosh Patil**. For help or collaboration, contact: `bsantoshkumar866@gmail.com`

---

Enjoy predicting the market trends! 📊