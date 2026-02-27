n=5
for i in range(2*n-1):
    for j in range(n):
        if(i+j<=n-1):
            print("* ",end="")
        elif(i-j>=n-1):
            print("* ",end="")
        else:
            print(" ",end="")
    print()
    '''
* * * * * 
* * * *  
* * *   
* *    
*     
* *    
* * *   
* * * *  
* * * * * 
    '''
