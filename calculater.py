def calculator():
    print("\n" + "="*40)
    print("Simple Calculator".center(40))
    print("="*40)
    
    while True:
        print("\nOperations available:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        try:
            operation = input("\nSelect an operation (1/2/3/4/5): ").strip()
            
            if operation == '5':
                print("\nThank you for using the calculator. Goodbye!")
                break
                
            if operation not in ('1', '2', '3', '4'):
                print("\n⚠️ Invalid input. Please select 1, 2, 3, 4, or 5.")
                continue
                
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("\n⚠️ Error: Please enter valid numbers only.")
                continue
                
            # Perform calculation
            if operation == '1':
                result = num1 + num2
                print(f"\nResult: {num1} + {num2} = {result}")
            elif operation == '2':
                result = num1 - num2
                print(f"\nResult: {num1} - {num2} = {result}")
            elif operation == '3':
                result = num1 * num2
                print(f"\nResult: {num1} * {num2} = {result}")
            elif operation == '4':
                if num2 == 0:
                    print("\n⚠️ Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"\nResult: {num1} / {num2} = {result}")
                    
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Exiting...")
            break
        except Exception as e:
            print(f"\n⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()