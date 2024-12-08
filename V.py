n = int(input("Enter the Vertical length of V: "))
a=1
b=n+n-1
for i in range(1,n+1):
    for j in range(1,b+1):
        if i == j or i+j == b+1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
