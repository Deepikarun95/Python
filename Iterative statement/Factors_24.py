############ Factorial of 24 #################

######### While loop ##############
n = int(input("enter the num :"))
i = 1
while i <= n :
    if n % i == 0:
        print(i)
    i += 1

########### For loop #########
n = int(input("enter the num :"))
i = 1
for i in range(i,n+1):
    if n % i == 0:
        print(i)
        i += 1