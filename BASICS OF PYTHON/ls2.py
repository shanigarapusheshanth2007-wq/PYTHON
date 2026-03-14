l1 = [1,2,4]
l2 = [1,3,4]
i=0
j=0
l=[]
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        l.append(l1[i])
        i=i+1
    else:
        l.append(l2[j])
        j=j+1
while i<len(l1):
    l.append(l1[i])
    i=i+1
while j<len(l2):
    l.append(l2[j])
    j=j+1
print(l)