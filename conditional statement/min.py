#########print the minimum in given number#########

#####using conditional statement###############
a = int(input("A      :"))
b = int(input("B      :"))
c = int(input("C      :"))
if (a < b) and (a < c):
    print("{} is the smallest number".format(a))
elif (b < c) and (b < a):
    print("{} is the smallest number".format(b))
else:
    print("{} is the smallest number".format(c))


###########using built in functions#######
min_number = min(a, b, c)
print("The minimum number is:", min_number)

########sorted futn##########
sorted_numbers = sorted([a, b, c])
min_number = sorted_numbers[0]