#to check the given number divisible by 7 or not
#in simple if else conditional statement and using function 

'''#####using simple if else statement###########
num =(int(input("enter the value :")))
if num % 7 == 0:
    print("the number is divisible by 7")
else:
    print("the number is not divisible by 7")'''


######## Using function statement#############
def div():
    num=int(input("enter the number"))
    if num % 7 == 0:
        print("the number is divisible by 7")
    else:
        print("the number is not divisible by 7")

div()

