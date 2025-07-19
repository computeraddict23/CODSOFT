while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Power")
    print("8. Exit")

    choice = input("Choose 1-8: ")

    if choice == '8':
        print("Goodbye!")
        break

    if choice not in ['1','2','3','4','5','6','7']:
        print("Invalid choice. Try again.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b == 0:
            print("Cannot divide by 0.")
        else:
            print("Result:", a / b)
    elif choice == '5':
        if b == 0:
            print("Cannot modulus by 0.")
        else:
            print("Result:", a % b)
    elif choice == '6':
        if b == 0:
            print("Cannot floor divide by 0.")
        else:
            print("Result:", a // b)
    elif choice == '7':
        print("Result:", a ** b)
