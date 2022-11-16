from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print("Welcome to the secret auction program.")

# def add_new_bidder(name, bidprice):
#     biddinglog = {}
#     biddinglog[name] = bidprice
#     #biddinglog.append(biddinglogdictio)
#     print(biddinglog)

def checkhighestbid(bidding_record):
    highestbid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highestbid:
            highestbid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestbid}")

bids = {}
shouldend = False
while not shouldend:
    name = input("Please provide your name: ")
    price = int(input("Please provide your bid price: $"))
    bids[name] = price
    otherbidder = input("Are there any other bidders? Type 'yes' or 'no' ")
    if otherbidder == "no":
        shouldend = True
        checkhighestbid(bids)
    elif otherbidder == "yes":
        clear()

