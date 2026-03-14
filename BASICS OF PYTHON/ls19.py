str="AABCAAADA"
len=len(str)
factors=[]
for i in range(1,len+1):
    if len%i==0:
        factors.append(i)
print(factors)
k=len(factors)
list=[]
for i in range(k):
    m=str[k*i:k*(i+1)-1]
    m=set(list(m))
    list.append(m)
print(list)