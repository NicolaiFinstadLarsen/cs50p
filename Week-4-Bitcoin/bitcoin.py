import requests
import sys

def main():
    # print(len(sys.argv))
    # print("yo")
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        try:
            num_of_bitcoin = float(sys.argv[1])
            # print(type(x))
        except ValueError:
            sys.exit(1) # Changed from 2 too 1 for check50
            
    if int(num_of_bitcoin):
        price = get_price(num_of_bitcoin)
        # if price:
        print(f"${price:,.4f}")
        # else:
            # sys.exit(3)
    else:
        sys.exit(3)

def get_price(n):

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    content = response.json()
    
    # This to prettyprint so I can understand what I am looking for.
    # print(json.dumps(content, indent=2))

    price = (content["bpi"]["USD"]["rate"])
    price = price.replace(",","")
    price = float(price)
    # Might need to return this variable and format later 
    
    # print(type(price))
    # print(type(n))

    return price * n
        
'''
To check error code in powershell use:
echo $LASTERRORCODE
'''    
main()