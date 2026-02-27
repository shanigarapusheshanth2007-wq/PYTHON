s="i am a baby boy53.  "#17 words
c=0
print(len(s))
for j in range(len(s)-1,0,-1):
    if(s[j]==" "):
        #print("x")
        while(s[j]==" "):
            #print("x")
            j=j-1
    while(s[j]!=" "):
        c=c+1
        j=j-1
    break
print(c)
