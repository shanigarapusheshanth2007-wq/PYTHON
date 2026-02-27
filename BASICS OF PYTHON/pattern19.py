for i in range(4):
    for j in range(7):
        if i<fj and i+j<4-1:
            if(j>=i):
                print(i+j+1,end="")
        elif(i+j>=4-1):
            if(i<j):
                print(j-i-1,end="")
        else:
            print(" ",end="")
    print()

        