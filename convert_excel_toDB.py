import pandas as pd
import sqlite3

file_path = "option-dhan-nifty.xlsx"
db_path = "options.db"

# Read only the necessary columns (adjust column indexes as needed)
df = pd.read_excel(file_path, usecols=[2, 7, 8, 11, 12, 16])  # Select key columns

# Connect to SQLite and save data
conn = sqlite3.connect(db_path)
df.to_sql("options", conn, if_exists="replace", index=False)

print("Database created successfully with selected columns!")
