#########print the minimum in given number#########

#####using conditional statement###############
a = int(input("A      :"))
b = int(input("B      :"))
c = int(input("C      :"))
if (a > b) and (a > c):
    print("{} is the max".format(a))
elif (b > c) and (b > a):
    print("{} is the max".format(b))
else:
    print("{} is the max".format(c))


###########using built in functions#######
#########max futn############
max_number = max(a, b, c)
print("The max number is:", max_number)



########sorted futn##########
sorted_numbers = sorted([a, b, c])
max_number = sorted_numbers[0]