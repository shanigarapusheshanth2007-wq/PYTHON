l=[1,2,3]
l=list(set(l))
l.sort()
m=l
k=[]
print(l,"-----")
for i in range(len(l)):
    m.sort()
    t=m[i]
    m[i]=m[0]
    m[0]=t
    m[1:].sort()
    for j in range(len(l)-1,0,-1):
        t=m[j-1]
        m[j-1]=m[j]
        m[j]=t
        print(m)
print(k)