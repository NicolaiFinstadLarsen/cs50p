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
            price = get_price(x)
        except ValueError:
            sys.exit(2)

    if price:
        print(f"{price:,}")
    else:
        sys.exit(3)

def get_price(n):
    '''
    get API call
    '''
    return 100_000 * n
        
    

main()