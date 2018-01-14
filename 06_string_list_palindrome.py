u_string = str(raw_input("Enter a string: "))

if u_string[0:len(u_string)] == u_string[::-1]:
	print(u_string + " is a palindrome")
else:
	print(u_string + " isn't a palindrome") 