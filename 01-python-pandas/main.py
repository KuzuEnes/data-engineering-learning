import pandas as pd

df = pd.read_csv('customers.csv')

df['amount'] = df['amount'].fillna(0)


def get_customer_level(amount):
    if amount >= 2000:
        return 'Gold'
    elif amount >= 1000:
        return 'Silver'
    else:
        return 'Bronze'

df['customer_level'] = df['amount'].apply(get_customer_level)

df.to_json('customer_with_level.json', orient='records', indent=4)