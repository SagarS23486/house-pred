import pandas as pd

# load dataset
data = pd.read_csv("Bengaluru_House_Data.csv")
data.columns = data.columns.str.lower()

# rename columns
data.rename(columns={
    'total_sqft': 'area',
    'bath': 'bathrooms',
    'bhk': 'bedrooms'
}, inplace=True)

# extract bedrooms if size exists
if 'size' in data.columns:
    data['bedrooms'] = data['size'].str.extract(r'(\d+)')
    data['bedrooms'] = pd.to_numeric(data['bedrooms'], errors='coerce')
    data.drop('size', axis=1, inplace=True)

# clean area
def convert_sqft(x):
    try:
        x = str(x)
        if '-' in x:
            a, b = x.split('-')
            return (float(a) + float(b)) / 2
        return float(x)
    except (ValueError, TypeError):
        return None

data['area'] = data['area'].apply(convert_sqft)

# clean location
data['location'] = data['location'].astype(str).str.strip()
data = data[data['location'] != 'nan']

# keep top locations
top_locations = data['location'].value_counts().head(50).index
data = data[data['location'].isin(top_locations)]

# convert numeric
for col in ['area', 'bedrooms', 'bathrooms', 'price']:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# keep only required columns
data = data[['area', 'bedrooms', 'bathrooms', 'location', 'price']]

# drop nulls
data = data.dropna()

# remove outliers based on price per sqft
data['price_per_sqft'] = data['price'] * 100000 / data['area']
data = data[(data['price_per_sqft'] >= 500) & (data['price_per_sqft'] <= 100000)]
data.drop('price_per_sqft', axis=1, inplace=True)

# remove unrealistic bedroom/bathroom counts
data = data[(data['bedrooms'] <= 10) & (data['bathrooms'] <= 10)]

# save clean data
data.to_csv("cleaned_housing.csv", index=False)

print("✅ cleaned_housing.csv ready")