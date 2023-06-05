###### print first 10 multiple of 4 ########


### for loop1 ########
for i in range(1,11):
    print(4*i)


### for loop 2 #######
for i in range(4, 41, 4):
    print(i)

###for loo########
n =int(input("enter the num :"))
for i in range(1,11):
    print(n*i,end=" ")

##### for loop3 ##############
n =int(input("enter the num :"))
count = 1
for i in range(1,11):
    x = i * n 
    print(x)
    count += 1

#######using while looop##########
n =int(input("enter the num :"))
count = 0
while n<=40:
    print(n)
    n = n + 4
    count += 0

