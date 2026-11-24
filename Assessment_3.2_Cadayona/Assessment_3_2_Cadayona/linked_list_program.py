# Assessment 3.2 - Linked List
# Last Name: CADAYONA

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_letters(self):
        for letter in "CADAYONA":
            new_node = Node(letter)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_node
        print("Letters added: CADAYONA")

    def remove_first(self):
        if self.head is None:
            print("The linked list is empty.")
        else:
            removed = self.head.data
            self.head = self.head.next
            print("Removed:", removed)

    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        values = []
        while current is not None:
            values.append(current.data)
            current = current.next
        print("Linked List:", " -> ".join(values))

linked_list = LinkedList()

while True:
    print("\n=== LINKED LIST MENU ===")
    print("1. Add letters of CADAYONA")
    print("2. Remove first letter")
    print("3. Display linked list")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        linked_list.add_letters()
    elif choice == "2":
        linked_list.remove_first()
    elif choice == "3":
        linked_list.display()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
