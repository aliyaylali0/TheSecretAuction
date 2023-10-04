print("Welcome to the secret auction program.")

bidder = {

}

"""name = input("What is your name? ")
bid = input("What's your bid?: $")
other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")"""

def ad_bidder(name,bid):
    bidder[name] = bid
    #print(bidder)

def big_bidder():
    big = max(bidder, key=bidder.get)
    bid_values = bidder[big]
    print(big,bid_values)


bidder_program = True

while bidder_program :
    name = input("What is your name? ")
    bid = input("What's your bid?: $")
    ad_bidder(name,bid)
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if other_bidder == "yes":
        bidder_program = True


    else:
        big_bidder()
        bidder_program = False


bidder = {

}
