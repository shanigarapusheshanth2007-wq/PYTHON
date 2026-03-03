s="sheshi"
y="heshis"
k=0
for i in range(len(s)):
    if(k+1>len(y)):
        print("its over")
        break
    if s[i]==y[k]:
        k=k+1
        print("ok lets go")
if k==len(y):
    print("ok its over sucess")
else:
    print("nooooo")
