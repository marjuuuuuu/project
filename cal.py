print("CHOOSE AN OPERATOR")
print("1. ADDITION")
print("2. SUBSTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
while True:
    theOperator = input("What do you want to do? ")

    if theOperator == "tapos na":
        break

    try:
		firstNumber = input("Enter First Number: ")
		secondNumber = input("Enter Second Number: ")
		
		if theOperator == "1":
			print("The sum is", str(float(firstNumber) + float(secondNumber)))
		elif theOperator == "2":
			print("The difference is", str(float(firstNumber) - float(secondNumber)))
		elif theOperator == "3":
			print("The product is", str(float(firstNumber) * float(secondNumber)))
		elif theOperator == "4":
			print("The average is", str(float(firstNumber) / float(secondNumber)))
        else:
            print("Invalid operator. Please enter 1, 2, 3, or 4")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


