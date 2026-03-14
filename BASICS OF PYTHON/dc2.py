y="banana"
s=list(y)
y=set(y)
for i in y:
    print(s.count(i))
d = {"a":1, "b":2, "c":3}
a=list(d.keys())
print(a[1])
b=list(d.values())
for i in range(len(d)):
    d.pop(a[i])
    d[b[i]]=a[i]
print(d)
m={
    "s":9.7,
    "y":9.3,
    "n":9.5
}
l=[k for k,v in m.items() if v==9.7]
print(l)
d1 = {"a":1, "b":2}
d2 = {"b":5, "c":4}
d1=d1|d2
print(d1)
d={**d1,**d2}#this method is known as unpacking
print(d)