import pandas as pd

def add_trend(df):
    df['temp_rolling'] = df['temperature'].rolling(window=30).mean()
    return df