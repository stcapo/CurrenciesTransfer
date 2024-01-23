from binance.client import Client
def main():
    l = [3,4,1]
    l.sort(key = lambda x:x!=4)
    print(l)
main()
