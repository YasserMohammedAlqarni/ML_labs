import pandas as pd
df = pd.read_csv('C:\\Users\\ThinkPad\\OneDrive\\سطح المكتب\\archive\\IntegratedData')
print(f"Dataset Shape: {df.shape}")
print("-" * 30)
print("First 5 rows:")
print(df.head())
print("-" * 30)
print("Dataset Info:")
df.info()
