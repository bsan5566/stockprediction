import streamlit as st
import pandas as pd
from utils.preprocessing import load_and_process
from utils.prediction import predict_lstm, predict_arima

st.set_page_config(page_title="Stock Predictor AI", layout="centered")
st.title("📈 Stock Price Prediction App")

uploaded_file = st.file_uploader("Upload your stock CSV file", type="csv")

if uploaded_file:
    df = load_and_process(uploaded_file)
    st.subheader("Raw Data Preview")
    st.write(df.tail())

    st.subheader("Closing Price Trend")
    st.line_chart(df['Close'])

    st.subheader("LSTM Prediction")
    forecast_lstm = predict_lstm(df)
    st.line_chart(forecast_lstm.set_index('Date')['Predicted_Close'])

    st.subheader("ARIMA Prediction")
    forecast_arima = predict_arima(df)
    st.line_chart(forecast_arima.set_index('Date')['Predicted_Close'])

    st.download_button("Download LSTM Forecast", forecast_lstm.to_csv(index=False), "lstm_forecast.csv", "text/csv")
    st.download_button("Download ARIMA Forecast", forecast_arima.to_csv(index=False), "arima_forecast.csv", "text/csv")