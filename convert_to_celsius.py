
import pandas as pd

df = pd.read_csv("data/raw/city_temperature.csv", low_memory=False)

# Check unique cities in India
india_cities = df[df['Country'] == 'India']['City'].unique()

print(india_cities[:50])   # show first 50
print("Total cities:", len(india_cities))