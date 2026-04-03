#Sales Data Analysis

#Goal: To analyze the sales data of a company and to identify the factors that affect the sales.

#step1: import pandas library
import pandas as pd
import numpy as np

data = {
    'Product':["Apple","Banana","Orange","Mango","Grapes"],
    'Price': [100,200,300,400,500],
}

df = pd.DataFrame(data)
print(df)

#step2:total sales per Product
sales_summary=df.groupby('Product')['Price'].sum()
print(sales_summary)

#step3: Using numpy for insights
sales_np=np.array(df['Price'])
print("Average sales:", np.mean(sales_np))
print("Maximum sales:", np.max(sales_np))
print("Minimum sales:", np.min(sales_np))