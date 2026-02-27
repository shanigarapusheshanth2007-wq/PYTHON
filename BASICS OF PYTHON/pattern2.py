n=5
for i in range(n+1):
    for j in range(n+1):
        if (i+j>=n):
            print("*",end="")
        else:
            print(" ",end="")
    print()