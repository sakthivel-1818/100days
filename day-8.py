def bids(bidders):
    high_amount = 0
    name = ""
    for list in bidders:
        amount=bidders[list]
        if amount>high_amount:
            high_amount=amount
            name=list

    print(f"The winner is {name} with a bid of ${high_amount}")



bid={}
game=True
while game:
    user=input("what is your name").lower()
    amount=int(input("how much did you bid $:"))
    bid[user]=amount

    another_bid=input("any another bid Yes or no").lower()
    if another_bid=="no":
        game=False

bids(bid)

