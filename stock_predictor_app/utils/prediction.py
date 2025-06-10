import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from statsmodels.tsa.arima.model import ARIMA

def predict_lstm(df):
    data = df['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    X, y = [], []
    for i in range(60, len(scaled_data)):
        X.append(scaled_data[i - 60:i, 0])
        y.append(scaled_data[i, 0])

    X, y = np.array(X), np.array(y)
    X = X.reshape(X.shape[0], X.shape[1], 1)

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=5, batch_size=64, verbose=0)

    last_60 = scaled_data[-60:]
    predictions = []
    input_seq = last_60.reshape(1, -1, 1)
    for _ in range(30):
        next_val = model.predict(input_seq, verbose=0)[0][0]
        predictions.append(next_val)
        input_seq = np.append(input_seq[:, 1:, :], [[[next_val]]], axis=1)

    forecast = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    dates = pd.date_range(start=df.index[-1], periods=31, freq='D')[1:]
    return pd.DataFrame({'Date': dates, 'Predicted_Close': forecast.flatten()})

def predict_arima(df):
    model = ARIMA(df['Close'], order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=30)
    dates = pd.date_range(start=df.index[-1], periods=31, freq='D')[1:]
    return pd.DataFrame({'Date': dates, 'Predicted_Close': forecast.values})