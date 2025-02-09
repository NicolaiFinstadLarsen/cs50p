import requests
import json

def main():
    
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    content = response.json()
    # This to prettyprint so I can understand what I am looking for.
    # print(json.dumps(content, indent=2))

    price = (content["bpi"]["USD"]["rate"])
    price = float(price.replace(",",""))
    print(f"{price:,.4f}")


main()