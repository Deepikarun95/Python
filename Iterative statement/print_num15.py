#######print number 15 to 10###########


############while loop###########
i=15
while i>=10:
    print(i)
    i=i-1
    
##########for#########
for i in range(15,9,-1):
    print(i)

#########function############

print("using function")
def display_num(n,i):
    if i >= n:
        print(i,n-1)    

display_num(10,15)