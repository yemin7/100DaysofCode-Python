import os

## Variables
auction_dict = {}
do_again = True

def auction( username, bid_amount):
    auction_dict[username] = bid_amount

def max_bid():
    winner, tmp_bid = '', 0
    for max in auction_dict:
        if auction_dict[max] > tmp_bid:
            tmp_bid = auction_dict[max]
            winner = max
    #winner = auction_dict.keys()[auction_dict.values().index(tmp_bid)]
    print(f"The winner is {winner} with bit amount {tmp_bid}")

while do_again:
    os.system("clear")
    name = input("What is your name? ")
    bid = int(input("Your bid amount. $"))
    auction(name, bid)
    print(auction_dict)
    result = input("Are there any other bidders? (yes/no)").lower()
    if result == "no":
        max_bid()
        do_again = False
