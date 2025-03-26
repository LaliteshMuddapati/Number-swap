n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

print("Before swapping: ", n1,n2,n3)

holder = 0


holder = n1
n1 = n2
n2 = n3
n3 = holder


print("After swapping: ", n1,n2,n3)
