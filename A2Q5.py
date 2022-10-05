#Question 5


c1x = float(input("Enter circle1's center x coordinate: "))
c1y = float(input("Enter circle1's center y coordinate: "))
c1r = float(input("Enter circle1's radius: "))

c2x = float(input("Enter circle2's center x coordinate: "))
c2y = float(input("Enter circle2's center y coordinate: "))
c2r = float(input("Enter circle2's radius: "))



if (  (c2y-c1y)**2 + (c2x-c1x)**2  )**0.5+ c2r <= c1r:
    print ("Circle 2 is inside circle 1")

elif (  (c2y-c1y)**2 + (c2x-c1x)**2  )**0.5 <= c1r + c2r:
    print ("Circle 2 overlaps circle 1")

else:
    print("Circle 2 doesn't overlap circle1")

