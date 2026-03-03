s="PAYPALISHIRING"
n=4
s=""
l=[]
for i in range(n):
    m=""
    k=0
    for j in range(k,len(s)):
        print("x")
        m=m+s[j]
        j=j+2*n-4*i-1
        if j>len(s):
            j=k
            break
    l.append(m)
print(l)
        
        