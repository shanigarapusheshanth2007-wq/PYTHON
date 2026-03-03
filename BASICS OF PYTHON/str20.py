l=['1','0','1','1','1','1','0','1','1','1','1','1']
m=0
for i in range(len(l)):
    c=1
    if l[i]=='1':
        for j in range(i+1,len(l)):
            if(l[i]==l[j]):
                c=c+1
             #   print(j,c,sep="----")
            else:
                break
        if c>m:
            m=c
        #print(m,"this is m")
print(m)

