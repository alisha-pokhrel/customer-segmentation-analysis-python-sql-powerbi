
# %% 
# IMPORT LIBRARIES

import pandas as pd


# %%
# DATA LOADING

file_path = r"C:\Users\alish\OneDrive\Desktop\customer_segmentation_anlaysis\customer_segmentation_analysis_5_years.xlsx"

excel_file = pd.ExcelFile(file_path)
print(excel_file.sheet_names)


# %%
# LOAD DATASETS

transactions_df = pd.read_excel(file_path, sheet_name="Transactions")
customer_df = pd.read_excel(file_path, sheet_name="Customers")
product_df = pd.read_excel(file_path, sheet_name="Products")


# %%
# TRANSACTIONS DATA EXPLORATION


# %%
# CUSTOMERS DATA EXPLORATION


# %%
# PRODUCTS DATA EXPLORATION
