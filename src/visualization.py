import matplotlib.pyplot as plt


def plot_temp(df, city, forecast=None):
    plt.figure(figsize=(14, 6))

    # 🔵 Actual temperature
    plt.plot(df['date'], df['temperature'],
             label='Actual Temperature', alpha=0.5)

    # 🔴 Trend
    plt.plot(df['date'], df['temp_rolling'],
             label='30-Day Trend', color='red')

    # ⚫ Anomalies
    anomalies = df[df['anomaly'] == 1]
    plt.scatter(anomalies['date'], anomalies['temperature'],
                color='black', label='Anomalies', s=10)

    # 🟢 Forecast
    if forecast is not None:
        plt.plot(forecast.index, forecast.values,
                 label='Forecast', color='green', linestyle='--')

    plt.title(f"Climate Trend & Forecast - {city}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    # Save graph
    plt.savefig(f"outputs/graphs/{city}_trend.png", dpi=300)
    plt.close()

    print(f"✅ Graph saved for {city}")