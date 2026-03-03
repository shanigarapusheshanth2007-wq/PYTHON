from collections import Counter
s="abba"
f=Counter(s)
c=0
for i,value in f.items():
    if(value%2!=0):
        c=1
if(c==1):
    print("no")
else:
    print("yes")