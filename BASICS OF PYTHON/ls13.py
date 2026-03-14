l=[4,5,6,7,0,1,2]
target=3
for i in range(len(l)):
    if l[i]>l[i+1]:
        print(i+1)
        k=i+1
        break
l=l[k:]+l[:k]
if target in l:
    print("x")