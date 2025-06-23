#Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    i=1
    while(i*i<=x):
        print (i*i , end = " ")
        i=i+1
        