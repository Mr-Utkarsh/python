# Ex1 - Getting and Knowing your Data

# Step 1. Import the necessary libraries

'''import numpy as np
import pandas as pd'''

# Step 2. Import the dataset

'''pd.read_csv("/Users/utkarshnageshwar/Desktop/code/pythonpandas/pandas_data.csv")'''

# Step 3. Assign it to a variable called a.

'''a=pd.read_csv("/Users/utkarshnageshwar/Desktop/code/pythonpandas/pandas_data.csv")
a'''

# Step 4. See the first 10 entries

'''a.head(10)'''

# Step 5. What is the number of observations in the dataset?

'''a.shape[0]'''

# Step 6. What is the number of columns in the dataset?

'''a.shape[1]'''

# Step 7. Print the name of all the columns.

'''a.columns'''

# Step 8. How is the dataset indexed?

# a.index
# a.info()

# Step 9. Which was the most-ordered item?
'''
b = a.groupby("item_name").agg({"quantity":"sum"})
c = b.sort_values("quantity",ascending = False)
c.head(1)'''

# Step 10. For the most-ordered item, how many items were ordered?

'''b = a.groupby("item_name").agg({"quantity":"count"})
c = b.sort_values("quantity",ascending = False)
c.head(1)'''

# Step 11. What was the most ordered item in the choice_description column?

'''b = a.groupby("choice_description").agg({"quantity":"sum"})
c = b.sort_values("quantity",ascending = False)
c.head(1)'''

# Step 12. How many items were orderd in total?

'''b = a.groupby("item_name").agg({"quantity":"count"})
c = b.sort_values("quantity",ascending = False)
c'''

# Step 13. Turn the item price into a float

'''a['item_price'] = a.item_price.str.slice(1).astype("float")'''

# Step 13.a. Check the item price type

'''a.item_price.dtype'''

# Step 14. How much was the revenue for the period in the dataset?

'''revenue=(a["quantity"]*a["item_price"]).sum()
revenue'''

# Step 15. How many orders were made in the period?

'''a.order_id.value_counts().count()'''

# Step 16. What is the average revenue amount per order?
'''
revenue=(a["quantity"]*a["item_price"])
revenue.mean()'''

# Step 17. How many different items are sold?

'''a.item_name.nunique()'''
