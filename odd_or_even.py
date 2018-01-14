#This program takes user input to see if the number entered is odd or even

def get_num():
	user_num = int(raw_input("Enter a number: "))

	choice = None
	while choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n':
		choice = str(raw_input("Would you like to enter a second (divider) number (Y/N): "))
		if choice == 'Y' or choice == 'y':
			divider = int(raw_input("Enter a second number: "))
			return choice, user_num, divider
		elif choice == 'N' or choice == 'n':
			divider = 2
			return choice, user_num, divider
		else:
			print(choice + " is not a valid option (Y/N)")

def divisible_by(choice, num, divisor):
	if num % 4 == 0:
		print("***** Yay! You've got yourself a multiple of 4! ******")
		print(str(num) + " is a multiple of 4. And an even number.")
	elif num % 2 == 0:
		print(str(num) + " is an EVEN number")
	else:
		print(str(num) + " is an ODD number")


	if choice == 'Y' or choice == 'y':
		if num % divisor == 0:
			print(str(num) + " is divisible by " + str(divisor))
		else:
			print(str(num) + " is not divisible by " + str(divisor))
	else:
		pass


quit = None
while quit != 'n' and quit != 'N':
	u_choice, u_num, u_div = get_num()
	divisible_by(u_choice, u_num, u_div)
	quit = str(raw_input("Would you like to continue (Y/N): "))
