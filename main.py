from dhanhq import dhanhq
import json
from dotenv import load_dotenv
import os
import sqlite3
import pandas as pd
import re

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
api_key = os.getenv("DHAN_API_KEY")
password = os.getenv("DHAN_PASSWORD")

dhan = dhanhq(api_key, password)

response = dhan.get_holdings()

data = json.dumps(response, indent=4)
print(data)

# Access data
for stock in response["data"]:
    print(f"Stock: {stock['tradingSymbol']}, Avg Price: {stock['avgCostPrice']}, LTP: {stock['lastTradedPrice']}")

option_name = input("Enter the option name: ").strip().lower()
option_name = re.sub(r'[-_]', '', option_name)  # Remove hyphens and underscores

db_path = "options.db"

# Connect to SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get column names dynamically
cursor.execute("PRAGMA table_info(options)")
columns = [col[1] for col in cursor.fetchall()]  # Fetch all column names

if len(columns) < 2:
    print("Error: The database does not have enough columns.")
    conn.close()
    exit()

second_column_name = columns[1]  # Get the second column name

# Use LOWER() in the query for case-insensitive search, and LIKE for partial matches
query = f"SELECT * FROM options WHERE LOWER(REPLACE({second_column_name}, '-', '')) LIKE ?"
cursor.execute(query, (f"%{option_name}%",))

# Fetch all matching rows
matching_rows = cursor.fetchall()

# Print results
if matching_rows:
    print("\nMatching Row(s):")
    for row in matching_rows:
        print(row)  # Print the full row as a tuple
else:
    print("\nNo matching option found.")

# Close the connection
conn.close()
