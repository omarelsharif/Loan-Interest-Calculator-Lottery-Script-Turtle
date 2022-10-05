#Question 4 
import random


coin = random.randint(0,1)
#print(coin)
guess = int(input("Guess head or tail? Enter 0 for head and 1 for tail: "))
if guess == coin:
    print("Correct guess")



if guess != coin:
    guess = "wrong"

if coin == 0:
    coin = "head"

if coin == 1:
    coin = "tail"

if guess == "wrong":
    print("Sorry, it is a", coin)
