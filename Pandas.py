import pandas as pd

# Extract
df = pd.read_csv('01-python-pandas/customers.csv')

# Transform
df['amount'] = df['amount'].fillna(0)
df['amount'] = df['amount'].astype(int)

df = df[df['amount'] > 1000]

# Load
df.to_csv('high_value_customers.csv', index=False)
df.to_json('high_value_customers.json', orient='records', indent=4)

df = pd.read_json('01-python-pandas/high_value_customers.json')

print(df.head())
print(df.dtypes)

