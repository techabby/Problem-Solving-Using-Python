# Write a program to find the maximum of three numbers.

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

if(a>b and b>c):
    print("The maximum of three numbers is ",a)
elif(a<b and b>c):
    print("The maximum of three numbers is ",b)
else:
    print("The maximum of three numbers is ",c)
    
