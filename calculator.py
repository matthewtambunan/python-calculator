# Python Calculator
def calculator():
    print("\n==============================")
    print("       PYTHON CALCULATOR")
    print("==============================")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nThank you for using Python Calculator!")
            break

        elif choice not in ["1", "2", "3", "4"]:
            print("\nError: Invalid operation. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = num1 + num2
                print("\nResult:", result)

            elif choice == "2":
                result = num1 - num2
                print("\nResult:", result)

            elif choice == "3":
                result = num1 * num2
                print("\nResult:", result)

            elif choice == "4":
                if num2 == 0:
                    print("\nError: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print("\nResult:", result)

        except ValueError:
            print("\nError: Please enter valid numbers.")

        print("\n------------------------------")


if __name__ == "__main__":
    calculator()
