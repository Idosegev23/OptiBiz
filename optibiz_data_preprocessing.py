import pandas as pd


def preprocess_data(data):
    # Clean and preprocess data
    data = data.dropna()  # Remove missing values
    data['purchase_date'] = pd.to_datetime(data['purchase_date'])  # Convert date to datetime format
    data['total_spent'] = data['price'] * data['quantity']  # Calculate total spent
    return data


# Example usage:
# data = pd.read_csv('customer_data.csv')
# preprocessed_data = preprocess_data(data)