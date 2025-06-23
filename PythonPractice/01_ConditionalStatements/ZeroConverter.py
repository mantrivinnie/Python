#You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.

#Note:- You don't have to return anything, you just have to print the array.

def pos(n):
    #write code here
    if n ==0:
        return "already zero"
    while n > 0:
        n -= 1
        print(n, end=" ")
        
def neg(n):
    #write code here
    if n ==0:
        return "already zero"
    while n <= 0:
        print(n, end=" ")
        n += 1  