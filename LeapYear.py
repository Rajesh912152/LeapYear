Year=int(input())
if (Year%4==0) and (Year%400==0 or Year%1!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")
