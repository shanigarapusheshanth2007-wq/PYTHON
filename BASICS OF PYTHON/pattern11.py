c=1
for i in range(5):
    for j in range(5):
        if i>=j:
            if(c%2==0):
                print("0 ",end="")
            else:
                print("1 ",end="")
            c=c+1
    print()
'''
1 
0 1 
0 1 0 
1 0 1 0 
1 0 1 0 1 
'''