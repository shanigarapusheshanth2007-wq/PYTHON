s = "PAYPALISHIRING"
l=[]
n=4
k=""
for j in range(5):
    i=j
    k=k+s[i]
    while i<len(s):
        a=i
        if i%(n-1)==0:
            i=i+2*n-2
            if i>=len(s):
                continue
            k=k+s[i]
            continue
        else:
            a=i
            fraction=(i)%(n-1)
            i=i+2*n-2-2*fraction
            b=i
            if i>=len(s):
                break
            k=k+s[i]
            #print(k)
            
            diff=2*n-2-b
            i=i+diff+a
            if i>=len(s):
                break
            #print(k)
            k=k+s[i]
            #i=i+2*n-2-2*fraction
            print(k)
            l.append(k)
            if len(l)==len(s):
                print("Sucess")
                break
print(l)
