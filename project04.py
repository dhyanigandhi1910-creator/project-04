print("Welcome to the Data Analyzer and Transformer Program")
data = []

def input_data():
    global data
    raw = input("Enter data for a 1D array (separated by spaces): ")
    data = list(map(int, raw.split()))
    print("Data has been stored successfully!")

def display_summary():
    print(f"- Total elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all values: {sum(data)}")
    print(f"- Average value: {round(sum(data)/len(data), 2)}")

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def filter_data():
    threshold = int(input("Enter a threshold value: "))
    filtered = list(filter(lambda x: x >= threshold, data))
    print("Filtered Data (values >= threshold):", filtered)

def sort_data():
    print("1. Ascending\n2. Descending")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Sorted Data:", sorted(data))
    elif choice == '2':
        print("Sorted Data:", sorted(data, reverse=True))

def dataset_stats():
    """Returns min, max, sum, avg"""
    return min(data), max(data), sum(data), round(sum(data)/len(data), 2)

def main():
    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary")
        print("3. Calculate Factorial")
        print("4. Filter Data by Threshold")
        print("5. Sort Data")
        print("6. Display Dataset Statistics")
        print("7. Exit Program")
        choice = input("Please enter your choice: ")

        if choice == '1':
            input_data()
        elif choice == '2':
            display_summary()
        elif choice == '3':
            num = int(input("Enter a number: "))
            print(f"Factorial of {num} is: {factorial(num)}")
        elif choice == '4':
            filter_data()
        elif choice == '5':
            sort_data()
        elif choice == '6':
            min_val, max_val, total, avg = dataset_stats()
            print(f"- Minimum value: {min_val}")
            print(f"- Maximum value: {max_val}")
            print(f"- Sum of all values: {total}")
            print(f"- Average value: {avg}")
        elif choice == '7':
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()




























