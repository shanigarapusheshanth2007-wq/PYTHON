l=["qwer","zxcvbnm","Hello","Aalaska","dad","pea"]
b="asdfghjkl"
a="qwertyuiop"
c="zxcvbnm"
for i in l:
    r=i.lower()
    r="".join(dict.fromkeys(r))
    print(r,"----")
    if(r[1] in a):
        counter=0
        for aa in range(len(r)):
            for bb in range(len(a)):
                if r[aa]==a[bb]:
                    counter=counter+1
        if counter==len(r):
            print(i)
    elif r[1] in b:
            counter=0
            for aa in range(len(r)):
                for bb in range(len(b)):
                    if r[aa]==b[bb]:
                        counter=counter+1
    if r[1] in c:
            counter=0
            for aa in range(len(r)):
                for bb in range(len(c)):
                    if r[aa]==c[bb]:
                        counter=counter+1
            if counter==len(r):
                print(i)

            


