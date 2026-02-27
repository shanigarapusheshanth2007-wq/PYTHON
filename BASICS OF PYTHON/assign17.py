i=0
while i<4:
    print("hello")
    i=i+1
n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in "sheshi nanan":
    if(i=='s' or i=='a'):
        continue
    else:
        print(f"after skipping {i}")
#making use of the pass statment
for i in "sheshi":
    pass
print(i)#it would give the answer as i beacuse it is run the loop it is like
#for (......); like in c but in python we have indentation we cant cretae a confusion so that we do this
for i in range(3):
    print(i)
var = 10
for i in range(10):
    for j in range(2,9):
        if var % 2 == 0:
            continue
        else:
            print(var)
            var += 1
print(var)

