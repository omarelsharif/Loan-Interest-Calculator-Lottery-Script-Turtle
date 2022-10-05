# Question 7

import random 
x = random.randint(100,999) # check if this is inclusive


print("Lottery is", x)
x = str(x)
number = str(int(input("Enter your lottery pick (three digits)")))




if str(number) == str(x):
    print("Exact match: Win $10,000")

    
elif (number[0] in x) and (number[1] in x) and (number[2] in x):
    
    print ("Match all digits: you win $3,000")
elif (number[0] in x) or (number[1] in x) or (number[2] in x):
    print ("Match 1: Win $1000")
   
else:
    print("Sorry, no match")




    



    


    
