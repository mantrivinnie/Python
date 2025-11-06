# Program to implement a Queue using List

queue = []  # empty queue

# Enqueue function
def enqueue():
    element = input("Enter element to enqueue: ")
    queue.append(element)
    print(f"{element} added to the queue.")

# Dequeue function
def dequeue():
    if not queue:
        print("Queue is empty! Cannot dequeue.")
    else:
        element = queue.pop(0)
        print(f"Dequeued element: {element}")

# Display function
def display():
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue elements are:")
        for i in queue:
            print(i, end=" ")
        print()

# Menu-driven queue operations
while True:
    print("\nChoose operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")
