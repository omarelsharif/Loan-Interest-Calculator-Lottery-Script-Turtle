#Question 1

from random import * 

x =  randint(12,36)
y =  randint(12,36)

z =  randint(12,36)




print ("x = ", x)
print ("y = ", y)
print ("z = ", z)





if x + 6 == 3 + y:
    print("x + 6 == 3 + y: -> True")
else:
    print("x + 6 == 3 + y: -> False")


if 2 * 6 - 4 >= 9 - z:
    print("2 * 6 - 4 >= 9 - z -> True")

else:
    print("2 * 6 - 4 >= 9 - z -> False")



if 6 // y < 3 - 1:
    print("6 // y < 3 - 1 -> True")

else:
    print("6 // y < 3 - 1 -> False")

if 18 // x == 2 * 3:
    print("18 // x == 2 * 3 -> True")

else:
    print("18 // x == 2 * 3 -> False ")


if x - y < 1:
    print ("not(x - y >= 1) -> True")
else:
    print ("not(x - y >= 1) -> False")
    


    
if z <= 7 or y < 12:
    print ("if z <= 7 or y < 12: True")

else:
    print ("if z <= 7 or y < 12: False")

 
if (x + y != 40) and (x != z):
    print("(x + y != 40) and (x != z) -> True")
else:
    print("(x + y != 40) and (x != z) -> False")


if (z - x >= y) or (y - x != z + 4):
    print ("(z - x >= y) or (y - x != z + 4) -> True")
else:
    print ("(z - x >= y) or (y - x != z + 4) -> False")

    
if (5 - x <= 2 * y) and (y -15 >= z)or (x - 5 != y  - 2 * z):
    print ("(5 - x <= 2 * y) and (y -15 >= z)or (x - 5 != y  - 2 * z) -> True")
else:
    print ("(5 - x <= 2 * y) and (y -15 >= z)or (x - 5 != y  - 2 * z) ->False")

if (True and False) or not (False or False) == True:
    print("(True and False) or not (False or False) -> True")

