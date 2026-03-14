l=[1,2,3,4,5,6,7,8]
print(l[0],l[-1],l[int(len(l)-1)//2])
l=[1,1,1,2,3,34,2,3,2,4,3,34,2]
l=list(set(l))
l.sort()
print(l)
Input=[4,5,1,2,1,6,2,4]
for i in Input:
    if Input.count(i)==1:
        print(i,"and i found it")
Input=[[1,2],[3,4],[5,6]]
l=[]
k=[Input[i][j] for i in range(len(Input)) for j in range(len(Input[i]))]
k=[0]*3
print(k)

