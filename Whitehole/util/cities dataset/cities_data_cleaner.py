import pandas as pd

# prunes the "worldcities.csv" and
# saves it to "worldcities_cleaned.csv"

df = pd.read_csv("worldcities.orignal.csv")
df = df[['city_ascii', 'lat', 'lng']]
df = df.rename(columns={
    'city_ascii': 'city',
    'lng': 'lon'
})
df['city'] = df['city'].str.lower()
df.to_csv("worldcities.csv", index=False)
