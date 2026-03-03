s="leetcode"
l=""
for i in s:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U' ):
        l=l+i
print(l)
# for reversing a string we can combine using slicing and reverse methos but slicing is the best option
r=""
for i in range(len(l)):
    r=l[i]+r
print(r)
k=""
z=0
for i in range(len(s)):
    if(s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U' ):
        k=k+r[z]
        z=z+1
    else:
        k=k+s[i]
print(k)
