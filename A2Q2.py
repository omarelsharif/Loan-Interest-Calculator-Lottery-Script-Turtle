# Question 2

weight1 = float(input("Enter the weight for package 1: "))
price1 = float(input("Enter the price for package 1: "))
value1 = price1/weight1

weight2 = float(input("Enter the weight for package 2: "))
price2 = float(input("Enter the price for package 2: "))
value2= price2/weight2

#print(value1)
#print(value2)



if value1 < value2:
    print("Package 1 has the best price.")

elif value1 == value2:
    print("Package 1 and 2 have the same price.")

else:
    print("Package 2 has the best price")
