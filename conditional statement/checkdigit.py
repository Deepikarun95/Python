#####check the digit######


num = int(input("enter the number"))
if num >= 1000 :
    print("four digit")
elif num >= 100:
    print("three digit")
elif num >=10 and num<10:
    print("two digit")
else:
    print("single digit number")
