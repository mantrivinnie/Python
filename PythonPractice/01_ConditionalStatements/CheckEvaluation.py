#Writing for loop in Python is a tad different from C++ and Java counterparts. In this question, we'll learn to print table by using the for loop.

#You are given a number N, you need to print its multiplication table.

def multiplicationTable(N):
    #code here
    for i in range(1,11):
        print(N*i, end=' ')