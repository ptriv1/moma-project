import pandas as pd

df = pd.read_csv('artworks.csv', dtype=str)

print("Columns:", df.columns.tolist())
print("Sample rows:", df.sample(5))

df.to_csv('artworks_cleaned_for_snowflake.csv', index=False, encoding='utf-8', quoting=1)
print("Cleaned CSV saved as artworks_cleaned_for_snowflake.csv")
