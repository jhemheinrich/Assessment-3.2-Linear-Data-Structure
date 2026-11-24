# Assessment 3.2 - Stack (LIFO)
# Last Name: CADAYONA

stack = []

def push_letters():
    for letter in "CADAYONA":
        stack.append(letter)
    print("Letters pushed:", " ".join(stack))

def pop_letter():
    if stack:
        print("Removed:", stack.pop())
    else:
        print("The stack is empty.")

def display_stack():
    if stack:
        print("Stack (bottom to top):", " ".join(stack))
        print("Top element:", stack[-1])
    else:
        print("The stack is empty.")

while True:
    print("\n=== STACK MENU ===")
    print("1. Push letters of CADAYONA")
    print("2. Pop top letter")
    print("3. Display stack")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        push_letters()
    elif choice == "2":
        pop_letter()
    elif choice == "3":
        display_stack()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
