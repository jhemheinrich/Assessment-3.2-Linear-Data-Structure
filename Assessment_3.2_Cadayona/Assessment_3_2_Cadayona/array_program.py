# Assessment 3.2 - Array
# Last Name: CADAYONA

letters = []

def add_letters():
    for letter in "CADAYONA":
        letters.append(letter)
    print("Letters added:", " ".join(letters))

def remove_letter():
    if letters:
        removed = letters.pop(0)
        print("Removed:", removed)
    else:
        print("The array is empty.")

def display_array():
    if letters:
        print("Array:", " ".join(letters))
    else:
        print("The array is empty.")

while True:
    print("\n=== ARRAY MENU ===")
    print("1. Add letters of CADAYONA")
    print("2. Remove first letter")
    print("3. Display array")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_letters()
    elif choice == "2":
        remove_letter()
    elif choice == "3":
        display_array()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
