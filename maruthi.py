def save_numbers_alphabetically():
    # Dictionary to store names and mobile numbers
    phone_book = {}

    while True:
        print("\nChoose an option:")
        print("1. Add/Update a Contact")
        print("2. Delete a Contact")
        print("3. Display Phone Book")
        print("4. Exit")
        
        # Input choice and handle errors
        choice = input("Enter your choice: ").strip()
        
        if choice == '4':
            print("Exiting the program.")
            break

        elif choice == '1':
            name = input("Enter Name: ").strip()

            # Validate name (only alphabetic characters allowed)
            if not name.isalpha():
                print("Invalid name. Please use only alphabetical characters.")
                continue

            mobile_number = input("Enter Mobile Number: ").strip()

            # Validate mobile number (10-digit number assumed for simplicity)
            if not mobile_number.isdigit() or len(mobile_number) != 10:
                print("Invalid mobile number. Please enter a 10-digit number.")
                continue

            # Add or update the entry in the dictionary
            phone_book[name] = mobile_number
            print(f"Contact for {name} has been added/updated.")

        elif choice == '2':
            name = input("Enter the Name to Delete: ").strip()

      
