import matplotlib.pyplot as plt
import re

def _safe_name(city):
    # remove parentheses and other non-alphanumeric, replace spaces with underscore
    name = re.sub(r'[()]', '', city)
    name = re.sub(r'[^0-9A-Za-z_.-]+', '_', name).strip('_')
    return name

def plot_temp(df, city, forecast=None):
    plt.figure(figsize=(14, 6))

    plt.plot(df['date'], df['temperature'], label='Actual Temperature', alpha=0.5)
    plt.plot(df['date'], df['temp_rolling'], label='30-Day Trend', color='red')

    anomalies = df[df['anomaly'] == 1]
    plt.scatter(anomalies['date'], anomalies['temperature'], color='black', label='Anomalies', s=10)

    if forecast is not None:
        plt.plot(forecast.index, forecast.values, label='Forecast', color='green', linestyle='--')

    plt.title(f"Climate Trend & Forecast - {city}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    safe = _safe_name(city)
    outpath = f"outputs/graphs/{safe}_trend.png"
    plt.savefig(outpath, dpi=300)
    plt.close()

    print(f"✅ Graph saved for {city} -> {outpath}")