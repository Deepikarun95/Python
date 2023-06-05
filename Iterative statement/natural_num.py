########cal the sum of natural numbers from 1 to 10###############
'''def cal_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i  
        return sum
    print(cal_sum(10))

cal_sum(11)'''


##########using for loop##########

n = int(input("enter the natural number upto :"))
sum = 0
for i in range(1,n+1):
    sum+=i
print("sum of the natural num",n,":",sum)

###########while#########

#n = int(input("enter the natural number upto :"))

sum = 0
i = 1
while i <= n:
    i += 1
    sum += i
print("number",sum)