c=1
for i in range(5):
    for j in range(5):
        if i>=j:
            print(f"{c} ",end="")
            c=c+1
        else:
            print(" ",end="")
    print()
'''
1     
2 3    
4 5 6   
7 8 9 10  
11 12 13 14 15 
'''