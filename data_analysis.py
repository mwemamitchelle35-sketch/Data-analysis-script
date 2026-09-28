import pandas as pd
import numpy as np

# 1. Load the dataset (Replace 'dataset.csv' with your file name if you upload one)
try:
    print("Loading dataset...")
    df = pd.read_csv('dataset.csv')
except FileNotFoundError:
    # Creating placeholder mock data if the file isn't uploaded yet
    print("Dataset file not found. Generating mock data for demonstration...")
    data = {
        'Region': ['North', 'South', 'East', 'West', 'North', 'East'],
        'Sales':,
        'Expenses': [8000, 11000, 6000, 14000, 9000, 7500]
    }
    df = pd.DataFrame(data)

# 2. Data Exploration & Overview
print("\n--- First 5 Rows of Data ---")
print(df.head())

print("\n--- Data Structure & Types ---")
print(df.info())

# 3. Data Cleaning (Handling missing values if any exist)
print("\nCleaning data...")
df = df.dropna()  # Drops missing values
df = df.drop_duplicates()  # Removes duplicate entries

# 4. Data Analysis & Insights
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Grouping data to find trends
if 'Region' in df.columns and 'Sales' in df.columns:
    print("\n--- Total Sales by Region ---")
    regional_sales = df.groupby('Region')['Sales'].sum()
    print(regional_sales)

print("\nAnalysis complete successfully.")
