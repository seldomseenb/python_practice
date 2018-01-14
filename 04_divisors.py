divisor = int(raw_input("For what number would you like to find divisors: "))

list_of_nums_less_than = range(1,divisor)
list_of_divisors = []

for i in list_of_nums_less_than:
	if divisor % i == 0:
		list_of_divisors.append(i)


print("List of divisors that evenly divide into " + str(divisor))
for j in list_of_divisors:
	print(j)