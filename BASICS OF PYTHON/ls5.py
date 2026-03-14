l= ["flower","flow","flight"]
s=""
for x in range(len(l[0])):
    if all(l[0][0:x] in y for y in l):
        s=l[0][0:x]
print(s)
l=["sheshanth","sheshi","shena","shepapa"]
s=""
for x in range(len(l[0])):
    if all(l[0][0:x] in y for y in l):
        s=l[0][0:x]
print(s)
l=["sheshansth","sheshisth","shenasth","shepapasth"]
s=l[0]
for x in l[1:]:
    while not x.endswith(s):
        s=s[1:]
        if s=="":
            break
print(s)
l=["sheshansth","sheshisth","shenasth","shepapasth"]
s=l[0]
for word in l[1:]:
    while not word.endswith(s):
        s=s[1:]
        if s=="":
            break
print(s)


