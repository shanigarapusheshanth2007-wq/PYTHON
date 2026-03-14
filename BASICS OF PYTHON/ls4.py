l=[1,2,3,4,5,6,3,2]
target=3
for i in range(len(l)):
    x=target-l[i]
    for j in range(len(l)):
        if x==l[j]:
            print(l[i],l[j])