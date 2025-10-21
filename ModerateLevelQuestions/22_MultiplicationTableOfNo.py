#To print a multiplication table of a number

def mulTable(n,x):
    for i in x:
        y = n*i
    return y

num = input("Enter the multiplication table number:")
table_till = input("Enter the table till digit:")
output = mulTable(num,table_till)
result = print("output is : " , output)
