s="abba"
y="do cat cat do"
r=y.split()
z=0
print(r)
for i in range(len(s)):
    for j in range(len(s)):
        if s[i]==s[j]:
            if(r[i]==r[j]):
                print("continue")
                z=1
            else:
                z=0
                print("sorrry bro ")
                break
if z==1:
    print("ok")
else:
    print("sorry")

    
                    
                    
                    

