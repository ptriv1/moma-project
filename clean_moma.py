import pandas as pd

df = pd.read_csv('artworks.csv') 

print("Before cleaning:", df['Date'].unique()[:10])

df['Clean_Year'] = df['Date'].astype(str).str.extract(r'(\d{4})')

print("After cleaning:", df[['Date', 'Clean_Year']].head(10))

df.to_csv('moma_artworks_cleaned.csv', index=False)