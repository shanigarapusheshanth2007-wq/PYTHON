s="PAYPALISHIRING"
n=5
k=""
i=1
j=0
l=[]
while j<=len(s):
    for i in range(len(s)):
        xxx=i
        k=""
        k=k+s[i]
        print(i)
        print("",k,"",sep="-----"*3)
        a=i
        i=2*n-2-i
        k=k+s[i]
        b=i
        if a+b!=2*n-2:
            k=k+s[a+b-2*n+2]
            j=j+3
            print(:)
        else:
            j=j+2
        l.append(k)
        i=xxx


print(l)
s="abcdefghijklmnopqrstuvwxyz"
j=0
n=6
l=[]
while j<=len(s):
        for i in range(len(s)):
            k=""
            a=i#store 1st value in a
            k=k+s[i]
            if i%(n-1)==0:
                 i=i+2*n-2
            else:
                 i=2*n-2-i%(n-1)
            b=i#stores 2nd value in b
            if i<len(s):
                 k=k+s[i]
            if i%(n-1)!=0 and i+a+2*n-2-b<len(s):
                k=k+s[i+a+2*n-2-b]
                j=j+2
            else:
                 j=j+3
            l.append(k)
print(l)