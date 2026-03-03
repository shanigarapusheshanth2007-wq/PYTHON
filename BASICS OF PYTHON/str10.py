s="aabbxxh"
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if(s[i]==s[j] and i!=j):
            c=c+1
    if(c==0):
        break
if(c==0):
    print("ok",s[i])
else:
    print("no")
            
