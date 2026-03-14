l=[10,20,10,30,20,40,50,30]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(j)
        if(j>=len(l)):
            break
        if l[i]==l[j]:
            l.pop(l[j])
            j=j+1
print(l)