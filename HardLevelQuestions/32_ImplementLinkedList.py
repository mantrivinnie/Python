# Program to implement a Linked List

# Node class to represent each element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"{data} inserted into the linked list.")

    # Function to delete a node by value
    def delete(self, key):
        current = self.head

        # If list is empty
        if current is None:
            print("Linked list is empty.")
            return

        # If head node holds the key
        if current.data == key:
            self.head = current.next
            print(f"Node with value {key} deleted.")
            return

        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with value {key} not found.")
            return

        # Unlink the node
        prev.next = current.next
        print(f"Node with value {key} deleted.")

    # Function to display the linked list
    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Driver Code (menu-driven)
linked_list = LinkedList()

while True:
    print("\nChoose operation:")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter value to insert: ")
        linked_list.insert(data)
    elif choice == 2:
        key = input("Enter value to delete: ")
        linked_list.delete(key)
    elif choice == 3:
        linked_list.display()
    elif choice == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")


