def main():
    while True:
        print("\nMenu:\n1. Greet User\n2. Check Even/Odd\n3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("\nHello! Welcome!")
        
        elif choice == "2":
            user_input = input("\nEnter an integer: ")
            try:
                number = int(user_input)
                if number % 2 == 0:
                    print(f"{number} is an Even number.")
                else:
                    print(f"{number} is an Odd number.")
            except ValueError:
                print("\nThat's not a valid number! Please enter an integer.")
        
        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()