#Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.

# Function to print x in decreasing order
def printInDecreasing(x):
    # Complete the code below
    while (x >= 0):

        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code
        print(x , end=" ")
        x -= 1