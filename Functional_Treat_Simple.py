# Data Analyzer and Transformer Program

print("Welcome to the Data Analyzer and Transformer Program")

data = []

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    # 1. Input Data
    if choice == "1":
        numbers = input("\nEnter data for a 1D array (separated by spaces): ")
        data = list(map(int, numbers.split()))
        print("\nData has been stored successfully!")

    # 2. Data Summary
    elif choice == "2":
        if not data:
            print("Please enter data first.")
        else:
            print("\nData Summary:")
            print("- Total elements:", len(data))
            print("- Minimum value:", min(data))
            print("- Maximum value:", max(data))
            print("- Sum of all values:", sum(data))
            print("- Average value:", round(sum(data) / len(data), 2))

    # 3. Factorial using Recursion
    elif choice == "3":
        n = int(input("\nEnter a number to calculate its factorial: "))

        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        print(f"\nFactorial of {n} is:", factorial(n))

    # 4. Filter using Lambda
    elif choice == "4":
        if not data:
            print("Please enter data first.")
        else:
            threshold = int(input(
                "\nEnter a threshold value to filter out data above this value: "
            ))

            filtered = list(filter(lambda x: x >= threshold, data))

            print("\nFiltered Data (values >= {}):".format(threshold))
            print(", ".join(map(str, filtered)))

    # 5. Sort Data
    elif choice == "5":
        if not data:
            print("Please enter data first.")
        else:
            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")

            sort_choice = input("\nEnter your choice: ")

            if sort_choice == "1":
                sorted_data = sorted(data)
                print("\nSorted Data in Ascending Order:")
                print(", ".join(map(str, sorted_data)))

            elif sort_choice == "2":
                sorted_data = sorted(data, reverse=True)
                print("\nSorted Data in Descending Order:")
                print(", ".join(map(str, sorted_data)))

            else:
                print("Invalid sorting choice.")

    # 6. Statistics using Multiple Return Values
    elif choice == "6":
        if not data:
            print("Please enter data first.")
        else:
            def statistics(numbers):
                minimum = min(numbers)
                maximum = max(numbers)
                total = sum(numbers)
                average = total / len(numbers)

                return minimum, maximum, total, average

            minimum, maximum, total, average = statistics(data)

            print("\nDataset Statistics:")
            print("- Minimum value:", minimum)
            print("- Maximum value:", maximum)
            print("- Sum of all values:", total)
            print("- Average value:", round(average, 2))

    # 7. Exit
    elif choice == "7":
        print("\nThank you for using the Data Analyzer and Transformer Program!")
        break

    else:
        print("\nInvalid choice. Please try again.")
