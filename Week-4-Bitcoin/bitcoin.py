import requests
import sys

def main():
    # print(len(sys.argv))
    # print("yo")
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        try:
            x = float(sys.argv[1])
            # print(type(x))
        except ValueError:
            sys.exit(2)
    price = get_price(x)
    # if price:
    print(price)
    # else:
        # sys.exit(3)

def get_price(n):

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    content = response.json()
    
    # This to prettyprint so I can understand what I am looking for.
    # print(json.dumps(content, indent=2))

    price = (content["bpi"]["USD"]["rate"])
    price = price.replace(",","")
    price = float(price)
    format_price = f"{price:,.4f}"

    # Might need to return this variable and format later 
    
    print(price)

    # return format_price * n
        
'''
To check error code in powershell use:
echo $LASTERRORCODE
'''    
main()