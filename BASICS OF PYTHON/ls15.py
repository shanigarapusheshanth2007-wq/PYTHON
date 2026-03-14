n=int(input("Enter number of students: "))
p=[]
f=[]
l=0
for i in range(n):
    k=int(input("Enter mark of student "))
    l=k+l
    if k > 40:
        p.append(k)
    elif k < 40 :
        f.append(k)
#print("Average Marks: "(average(p)))
print("Highest Marks: ",max(p))
print("Students Above Average:",(sum(p)+sum(f))/n)
for i in range(len(p)):
    print(p[i])
for i in range(len(f)):
    print(f[i])
print("Number of Students Passed: ",len(p))
print("Number of Students Failed: ",len(f))