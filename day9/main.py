import os
import art

os.system('clear')
print(art.logo)
done = False
bids = {}

while(not done):
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    bids[name] = int(bid)
    done = input("Are the other bidders? Type 'yes' if yes. ").lower() != "yes"
    os.system('clear')

winner = { "name": "", "bid": 0 }

for name in bids:
    if bids[name] > winner["bid"]:
        winner["name"] = name
        winner["bid"] = bids[name]

print(f"The winner is {winner['name']}, with a bid of {winner['bid']}.")
