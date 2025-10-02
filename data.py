import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df.head()        # First 5 rows
df.info()        # Data types
df.describe()    # Summary stats
df.shape         # (rows, columns)
sales_by_product = df.groupby("Product")["Sales"].sum()

sales_by_product.plot(kind="bar", figsize=(8,5))
plt.title("Sales by Product")
plt.show()

df.isna().sum()      # Find missing values
df.fillna(0, inplace=True)  # Example fix

