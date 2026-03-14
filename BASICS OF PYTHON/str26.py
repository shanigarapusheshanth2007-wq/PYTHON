s="abcdefghijklmnopqrstuvwxyz"
j=0
n=6
l=[]
i=0
m=0
while j<=n:
        while i<len(s):
            k=""
            if i>=len(s):
                 continue
            k=k+s[i]
            a=i
            if i%(n-1)==0:
                i=i+2*n-2
                if i>=len(s):
                 continue
                k=k+s[i]
                continue
            else:
                i=(2*n-2)*j+2*n-2-i%(n-1)
                b=i
                if i>=len(s):
                 break
                k=k+s[i]
                if i%(n-1)!=0 and i+a+2*n-2-b<len(s):
                    k=k+s[i+a+2*n-2-b]
                    i=i+a+2*n-2-b
                m=m+len(k)
                print(k)
                if i==len(s)-1 and m==len(s):
                    break
        l.append(k)
        j=j+1  
print(l)