import pandas as pd
from src.trend_analysis import add_trend
from src.anomaly_detection import detect_anomalies
from src.forecasting import prepare_time_series, train_arima_model, forecast_temperature
from src.visualization import plot_temp


def main():
    print("🚀 Running Climate Analyzer for SELECTED cities...\n")

    # Load cleaned dataset
    df = pd.read_csv("data/processed/clean_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])

    # Selected cities
    selected_cities = [
        'Bombay (Mumbai)',
        'Calcutta',
        'Chennai (Madras)',
        'Delhi'
    ]

    print("Selected Cities:", selected_cities)

    for city in selected_cities:
        print(f"\n📍 Processing City: {city}")

        city_df = df[df['City'] == city]

        if city_df.empty:
            print("⚠️ No data found for this city. Skipping...")
            continue

        print("Shape:", city_df.shape)

        # Trend
        city_df = add_trend(city_df)

        # Anomaly
        city_df = detect_anomalies(city_df)

        print("🚨 Anomalies:", city_df['anomaly'].sum())

        # Forecast
        ts_df = prepare_time_series(city_df)
        model = train_arima_model(ts_df)
        future = forecast_temperature(model)

        print("📈 Forecast:")
        print(future.head())

        # Visualization (with forecast)
        plot_temp(city_df, city, future)


if __name__ == "__main__":
    main()