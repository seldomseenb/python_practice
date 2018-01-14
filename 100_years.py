#This program takes the user age and tells when they will turn 100 years old


def get_name():
	user_name = str(raw_input("Enter your name: "))
	print("Your name is " + user_name)

	return user_name

def get_age():
	user_age = int(raw_input("Enter your age: "))
	print("Your current age is " + str(user_age))

	return user_age

def calc_100(user_age):
	years_till_100 = 100 - user_age
	year_of_100 = str(2017 + years_till_100)
	print(name + " you will be 100 years old in the year " + year_of_100)


name = get_name()
age = get_age()
calc_100(age)