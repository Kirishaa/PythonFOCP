#reads the input data given by user
number = input("Enter a number: ")
#the input always takes strings so the below statement changes string to integer
number = int(number)
#prints the statement and the number
print("The numbered entered was", number)
#the statement block below checks if the number is even or odd
if (number % 2) == 0:
    print("That is an even number")
    if (number%10)==0:
        print("The number is divisible by 10.")
    else:
        print("The number is not divisible by 10.")
else:
	print("That is an odd number")
