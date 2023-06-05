#####given numbers in ascending order using ########
#############sorting###########
a1=[5,8,2,9,45,65,25,78]

a1.sort()
print(a1)


####using conditional statement#########
num1=int(input("aa   :"))
num2=int(input("bb   :"))
num3=int(input("cc   : ")) 
if num1<num2 and num1<num3:
    if num2<num3:
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)
elif num2<num1 and num2<num3:
    if num1<num3:
        print(num2,num1,num3) 
    else:
        print(num2,num3,num1)
else:
    if num2<num1:
        print(num3,num2,num1)
    else:
        print(num3,num1,num2)

##################using iteration statement##########
a=[50,90,30,68,95,74,15,21,24,56,35,98]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)



    