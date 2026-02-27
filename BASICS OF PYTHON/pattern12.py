for i in range(1,5,1):
    for j in range(1,9,1):
        if(i+j>=5 and abs(i-j)<=3):
            if(j<=4):
                print(5-j,end="")
            elif(j>4):
                print(j-3,end="")
        else:
            print(" ",end="")
    print()
    '''
   1    
  212   
 32123  
4321234 
    '''