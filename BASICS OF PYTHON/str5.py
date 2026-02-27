s=int(input("Enter a number"))
digits=1
a=26
for i in range(2,5):
    if(s>a):
        a=a+26**i
    elif(s==a):
        print(i-1)
        break
    else:
        print(i-1)
        break
    #r=(s-26)%26
    #q=(s-26)//26
    #print(chr(q+65),chr(r+64))