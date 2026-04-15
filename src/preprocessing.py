# ===============================
# FILE: preprocessing.py
# PURPOSE: Clean climate dataset
# ===============================

import pandas as pd


def clean_climate_data(file_path):
    """
    Loads and cleans climate dataset
    """

    # 🔹 Step 1: Load data
    df = pd.read_csv(file_path, low_memory=False)

    print("Initial Shape:", df.shape)

    # 🔹 Step 2: Remove duplicate rows
    df = df.drop_duplicates()
    print("After removing duplicates:", df.shape)

    # 🔹 Step 3: Handle missing values

    # Drop rows where temperature is missing
    df = df.dropna(subset=['AvgTemperature'])

    # Fill missing State with 'Unknown'
    df['State'] = df['State'].fillna('Unknown')

    # 🔹 Step 4: Create Date column
    df['date'] = pd.to_datetime(df[['Year', 'Month', 'Day']], errors='coerce')

    # Remove rows where date is invalid
    df = df.dropna(subset=['date'])

    # 🔹 Step 5: Convert temperature (F → C)
    df['Temp_C'] = (df['AvgTemperature'] - 32) * 5/9

    # 🔹 Step 6: Remove unrealistic values
    # (Extreme values can be sensor errors)
    df = df[(df['Temp_C'] > -50) & (df['Temp_C'] < 60)]

    # 🔹 Step 7: Sort data by date
    df = df.sort_values('date')

    # 🔹 Step 8: Reset index
    df = df.reset_index(drop=True)
    
    df.rename(columns={'AvgTemperature': 'temperature'}, inplace=True)
    
    print("Final Cleaned Shape:", df.shape)

    return df


# Optional: Save cleaned data
def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")