from dhanhq import dhanhq
import json
from dotenv import load_dotenv
import os

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
    