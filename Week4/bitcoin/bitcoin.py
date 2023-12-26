import requests
import sys
import json

# get value from command-line
if len(sys.argv) == 2:
    try:
        sys.exit("Command-line argument is not a number")
    except:
        pass
else:
    sys.exit("Missing command-line argument")
# price of Bitcion = b with value of command-line
try:
    read = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    act = read.json()
    b = act["bpi"]["USD"]["rate_float"]
    amount = b * float(sys.argv[1])
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit("RequestException")