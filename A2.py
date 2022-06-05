# Python program to print positive Numbers in given range
 
a = int(input("Enter the start of range: "))
b = int(input("Enter the end of range: "))
for num in range(a,b + 1):
    if num >= 0:
        print(num, end = " ") 
