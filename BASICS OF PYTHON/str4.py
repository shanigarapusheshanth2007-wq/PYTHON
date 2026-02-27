s="A man, a plan, a canal: Panama"
s=s.lower()
l=""
c=0
for i in s:
    if (ord(i)>=48 and ord(i)<=57) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        l=l+i
        c=c+1
print(l)
m=""
for j in range(len(l)-1,-1,-1):
    m=m+l[j]
print(m)
if(l==m):
    print("sucess")