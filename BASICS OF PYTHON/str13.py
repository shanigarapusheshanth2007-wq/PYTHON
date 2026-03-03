s="nananss"
z=0
k=0
for i in range(len(s)):
    c=1
    if s[i]=='x':
       continue
       print("err")
    for j in range(i+1,len(s)):
      if s[j]=='x':
         continue
         print("err")
      if s[i]==s[j] and i!=j:
        c=c+1
        s=s[:j]+'x'+s[j+1:]
        print(s)
    print(s[i],c,sep="---")
    if c%2==0:
       z=z+c
    else:
       z=z+c-1
       k=1
print(s)
if k==1:
   print(z+1)
else:
   print(z)

