'''l=["apple","nanan","papas","jamuuu"]
if "apple" in l:
    print("x")
#it only checks the elments of the l not go into the l if the inner one is a list or tuple
l=[["apple"],"nanan","papas","jamuuu"]
if ["apple"] in l:
    print("Apple list is present")
    print(type(["apple"]))
l=["i like apple","but i ate banana"]
#if "apple" in l:
#     print("x")not works because the apple is here in the inner loop
for item in l:
    if "apple" in item:
        print("Apple found inside element")
l=["nana","papa","nenu"]
l[1:3]=["nnnn","iii"]#here the index 3 is excluded in the list
print(l)
l[1:3]=["nan"]#here the l[2] is deleted in this list 
print(l)#output is ['nana', 'nan']
l=["nana","papa","nenu"]
l[1:2]=["nnn","jjj"]# means here we are adding 2 elmenys in b/w the elements in the place of 1
print(l)
print(len(l))
l=["nana","papa","nenu"]
l[1:3]=["a","b","c","d"]
print(l)#['nana', 'a', 'b', 'c', 'd']replaced 1 and 2 and if extra elements needed it goes and extends the list
print(len(l))
l=["nana","papa","nenu"]
l[1:3]=["pppp"]
print(l)
print(len(l))
#insert method
l=["nana","papa","nenu"]
l.insert(1,[1,2,3])
print(l)
l.append("sheshanth")
print(l)
#extending a list
m=["k","l","m"]
l.extend(m)
print(l)#output is ['nana', [1, 2, 3], 'papa', 'nenu', 'sheshanth', 'k', 'l', 'm']
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).like i thought
#i can add two lisst and get the same but i can do it with dict and tuple and sets also
s={1,2,3}
l.extend(s)
print(l)
l=[1,2,3,2,1,2,1,2,1,2,2]
l=set(l)
print(list(l))
r=[]
r.extend(l)
print(r)
thislist = ["apple", "banana", "cherry"]
thislist.remove(thislist[2])#removes the first occurence of the term like
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")#removes the first occurence of the term like
print(thislist)
l = [" apple ", "  banana ", "  cherry "]
print("".join(l))
print(l)
print(type(l))
l= ["apple", "banana", "cherry"]
l.remove(l[1])
del l[1]#as it as l.remove()
print(l)
l= ["apple", "banana", "cherry"]
del l[0:2]
print(l)
#del can del any number of elements at one time but remove cant remove more than one element at a time
#The del keyword also removes the specified index:
#The clear() method empties the list.
l=["a","b","c","d"]
l.clear()
print(l)
l=["a","b","c","d"]
[print(x) for x in l]
fruits = ["apple", "banana....", "cherry", "kiwi", "mango"]
n=[x for x in fruits if "a" in x]
print(n)
n=[x for x in fruits if "apple" not in x]
print(n)
n=[x for x in range(1,10)]
print(n)
n=[x.upper() for x in fruits]
print(n)
n=[x.strip(".").upper() for x in fruits]
fruits = ["....apple", "....banana....", "....cherry", "....kiwi", "...mango"]
print(n)
n=[x.strip(".") if x!="banana" else "orange" for x in fruits]
print(n)
fruits = ["apple","zzz", "banana", "cherry", "kiwi", "mango"]
fruits.sort()
print(fruits)
fruits.sort(reverse =True)
print(fruits)
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort(key = str.lower)
print(fruits)
fruits.reverse()
print(fruits)#reverses the list regardless of any thing'''
fruits = ["banana", "Orange", "Kiwi", "cherry"]
#if we wanna make a copy of a list dont give it as l=m just do the below
n=fruits.copy()
print(n)
#another way is below method
n=list(fruits)
print(n)
#count
l=[1,1,2,3,4,5,5,6,4,5,3,4,3,3,2]
print(l.count(3))
