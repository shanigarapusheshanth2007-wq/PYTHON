for i in range(9):
    for j in range(9):
        a=abs(5-i)+abs(5-j)
        if(a<=3):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    '''
          *       
        * * *     
      * * * * *   
    * * * * * * * 
      * * * * *   
        * * *     
          *  
    '''