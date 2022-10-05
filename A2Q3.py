#Question 3


number = int(input("Enter an integer: "))

if number%5==0 and number%6==0:
        
    print(str(number), "is divisible by both 5 and 6")

elif number%5 !=0 and number%6 != 0:
    print(str(number), "is not divisible by either 5 or 6")

else:
    print(str(number), "is divisible by 5 or 6, but not both")

