from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print (logo)
print ("Welcome to the secret auction program.")

bidder_dictionary = {} #empty dictionary to add name and bid amount

continue_bid = True #condition to end while loop 

while continue_bid == True:

  name = input("What is your name?: ").lower()
  bid = int(input("What's your bid?: $"))
  others = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  
  bidder_dictionary[name] = bid
  if others == "no":
    continue_bid = False
    clear()
  else:
    clear()

bidder_check = 0
bidder_name = ""
for name in bidder_dictionary:
    if bidder_dictionary[name] > bidder_check:
      bidder_check = bidder_dictionary[name]
      bidder_name = name
print (f"The winner is {bidder_name} with a bid of {bidder_check}")

print (bidder_dictionary)


