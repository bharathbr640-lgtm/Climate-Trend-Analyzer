# =====================================
# FILE: forecasting.py
# PURPOSE: Train ARIMA model for temp prediction
# =====================================

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def prepare_time_series(df):
    df = df[['date', 'temperature']]
    df = df.set_index('date')

    # Resample daily
    df = df.resample('D').mean()

    # Fill missing values
    df = df.ffill()

    return df
    


from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(df):
    print("Training ARIMA model...")

    model = ARIMA(df['temperature'], order=(2, 1, 2))
    model_fit = model.fit()

    print("Model training completed!")

    return model_fit

def forecast_temperature(model_fit, steps=30):
    """
    Forecast future temperatures
    """
    forecast = model_fit.forecast(steps=steps)
    return forecast