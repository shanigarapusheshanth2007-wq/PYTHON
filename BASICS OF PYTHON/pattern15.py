n=1
for i in range(n):
    for j in range(n):
        if(i>=j):
            if(i+j<n-1):
                print("* ",end="")
            else:
                print("  ",end="")
        elif(j>i):
            if(i+j>=n-1):
                print("* ",end="")
            else:
                print("  ",end="")
    print()
'''
*                   * 
* *               * * 
* * *           * * * 
* * * *       * * * * 
* * * * *   * * * * * 
* * * * *   * * * * * 
* * * *       * * * * 
* * *           * * * 
* *               * * 
*                   * 
                      '''