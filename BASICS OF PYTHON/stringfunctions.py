'''Docstring for PYTHON.PYTHON.BASICS OF PYTHON.stringfunctions
s="SHeshYanana"
print(s.upper())
print(s.lower())
a="    hello world.   "
print(a.strip())
a="hello world"
s="she-shan-anan"
print(a.replace("h","z"))
print(b.replace("-",""))#also knownn as the remove method
a3="he i am a man"
print(a.split(" ,"))
l=a.split()
print(l)
a, b = input().split()
input().split() #creates a list, for example: ["10", "20"].
a,b=map(int,input().split())#takes the input as int
print(type(a),b)
numbers = (map(int, input().split()))
print(numbers)
for x in map(int,[1,2,3,5]):
    print(x)
z=f"this is the thing format('x','-^5') i have done"
print("this is the thing format('x','-^5') i have done",format('x','-^5'))
i=2
if i in range(1,5):
    print(i)
s="sheshi"
print(s.capitalize())
s="SHESHI"
print(s.casefold())
#case fold is same as lower but the main applicarion is
s1 = "ß"        # German sharp S
print(s1.lower())
print(s1.casefold())
output
ß
ss
✅ Another Example (Case-Insensitive Compare)
a = "Straße"
b = "STRASSE"

print(a.lower() == b.lower())
print(a.casefold() == b.casefold())
output
False
true
#👉 casefold() correctly detects they are equal.
s="sheshi"
print(s.center(10))# it is same like as format(x,' ^10')
print(s.center(8,'-'))
##count 
x="i am sheshi"
print(x.count("sh"))#counts the no of repetations
x="i am sheshi i am sheshi i am sheshi"
print(x.count("sheshi",0,15))# saying that only count from x[0] to x[15]
#The endswith() method returns True if the string ends with the specified value, otherwise False.
x="sheshi"
if x.endswith("i",3,6):
    print("ok")\
#string.expandtabs(tabsize)
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
#find method
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
s="sheshanth"
if s.find("she",2,7):
    print("ok")
s={"name":"sheshi","age":20}
x="his name is {name} and age is {age}"
x=x.format_map(s)
print(x)#his name is sheshi and age is 20  string.format_map(dictionary)
g={"name":"rani","age":23,"roll":20222}
t="my name is {name} and roll is {roll}"
t=t.format_map(g)
print(t)
s="his name is rama"
#print(s.index("ei"))# return errror if not found 
print(s.index("e"))
print(s.find("ei"))#return -1 if not found
print(s.index("e",3,8))#start end also can be put in it
# is alum to check wether it is a alpha numeric number
s="12jvbosp"
print(s.isalnum())
y="123456[sdfg]"
print(y.isalnum(),)
s="9876000"
print(s.isdecimal())#return if it is a number
print(s.isdigit())#return if it is a number more strict
#is identifier is know that is avalid name of a variable
#like if name of varibale is 1ab is wrong return -1 i abhi is corecr
aa=1
s='1a'
y='aa'
print(s.isidentifier())
print(y.isidentifier())
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
#join method
#.  "place the thing that you want to insert in b/w them"join(list/tuple)
l=["nan","yes","sheshu"]
r="".join(l)
print(r)#nanyessheshu is the output
l=["aabbcc","abcabc","abcabc"]
r="aabbcc"
#r="".join(dict.fromkeys(r))
r="-".join(r)
print(r)#a-a-b-b-c-c is output
print(l)
l="-".join(dict.fromkeys(l))
print(l)
o=("sheshi","paps","kana")
r="#".join(o)#sheshi#paps#kana is the output
print(r)
#left justified as like as format(,'>5')
x="banana"
print(x.ljust(20,"-"))# banana-------------- is the output
#right justified
print(x.rjust(20,"-"))#--------------banana is the output
#centre
print(x.center(20,"-"))# -------banana------- is the output
#remove a specfic charecter like 
x="-------,,,,,banana"
print(x.lstrip("-,"))#banana is the output
print(x.lstrip("-"))#,,,,,banana output
print(x.lstrip(",-"))#banana is the output same as lstrip("-,")
s="shesssssshanthssss"
print(s.lstrip("s"))#only removes the charecters from the front side only
#partion
x="my name is sheshi nana and i am she"
print(x.partition("sheshi"))#('my name is ', 'sheshi', ' nana and i am she') it is a tuple with partions
#replace
x="a is the a for all a and a"
r=x.replace("a","😀",4)#4 species only r a's are replaceed by the 😀
print(r)
print(r.partition("a"))
#find and rfind
x=" i am sheshi and i"
print(x.find("i"))#returns the first occurence of a string
print(x.rfind("i"))#return the index of last occurence of a string
#index and rindex
print(x.index("a"))#return the index as same as dfind but small diff
print(x.rindex("a"))#returns the last occurence as same as rfind
#partion and r partion and l partition (l is not there)
x="it is a banana,i love banana,i hate banana"
print(x.partition("banana"))#('it is a ', 'banana', ',i love banana,i hate banana')
print(x.rpartition("banana"))#('it is a banana,i love banana,i hate ', 'banana', '')
#rsplit is same as split but string.rsplit(separator, maxsplit) we can specify 
#from right side that how many splits
#strip rstrip lstrip
x'''