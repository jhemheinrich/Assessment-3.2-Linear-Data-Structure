# Assessment 3.2 - Queue (FIFO)
# Last Name: CADAYONA

queue = []

def enqueue_letters():
    for letter in "CADAYONA":
        queue.append(letter)
    print("Letters added:", " ".join(queue))

def dequeue_letter():
    if queue:
        removed = queue.pop(0)
        print("Removed:", removed)
    else:
        print("The queue is empty.")

def display_queue():
    if queue:
        print("Queue (front to rear):", " ".join(queue))
    else:
        print("The queue is empty.")

while True:
    print("\n=== QUEUE MENU ===")
    print("1. Enqueue letters of CADAYONA")
    print("2. Dequeue first letter")
    print("3. Display queue")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        enqueue_letters()
    elif choice == "2":
        dequeue_letter()
    elif choice == "3":
        display_queue()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
