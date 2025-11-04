# Program to implement a Stack using List

stack = []  # empty stack

# Push function
def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(f"{element} pushed into stack.")

# Pop function
def pop():
    if not stack:
        print("Stack is empty! Cannot pop.")
    else:
        element = stack.pop()
        print(f"Popped element: {element}")

# Display function
def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack elements are:")
        # Display top at the bottom for clarity
        for i in reversed(stack):
            print(i)

# Menu-driven stack operations
while True:
    print("\nChoose operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")


"""Choose operation:
1. Push
2. Pop
3. Display
4. Exit
Enter your choice: 1
Enter element to push: 10
10 pushed into stack.

Enter your choice: 1
Enter element to push: 20
20 pushed into stack.

Enter your choice: 3
Stack elements are:
20
10

Enter your choice: 2
Popped element: 20
"""


#Explanation:
#A stack follows LIFO (Last In First Out) principle.
#append() → used to push elements.
#pop() → used to remove the top element.