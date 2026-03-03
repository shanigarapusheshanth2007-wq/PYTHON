s="123"
y="179"
t=0
z=0
f=0
for i in range(len(s)-1,-1,-1):
    k=int(s[i])
    #print(s[i])
    z=z+k*10**f
    f=f+1
print(z)
f=0
k=0
for i in range(len(s)-1,-1,-1):
    k=int(y[i])
    print(y[i])
    t=t+k*10**f
    f=f+1
print(t+z)
