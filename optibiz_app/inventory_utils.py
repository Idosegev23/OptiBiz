import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import timedelta

# Calculate inventory turnover ratio
def inventory_turnover(sales, average_inventory):
    turnover = sales / average_inventory
    return turnover

# Calculate days of inventory on hand
def days_of_inventory_on_hand(inventory_turnover):
    days = 365 / inventory_turnover
    return days

# Implement a simple linear regression forecasting method
def forecast_sales(sales_data, days_to_forecast):
    sales_data = np.array(sales_data)
    days = np.array(range(len(sales_data)))
    
    # Fit linear regression model
    model = LinearRegression().fit(days.reshape(-1, 1), sales_data)
    
    # Predict future sales
    future_days = np.array(range(len(sales_data), len(sales_data) + days_to_forecast))
    forecasted_sales = model.predict(future_days.reshape(-1, 1))
    
    return forecasted_sales

# Determine reorder points
def reorder_points(lead_time, daily_sales, safety_stock):
    reorder_point = lead_time * daily_sales + safety_stock
    return reorder_point
