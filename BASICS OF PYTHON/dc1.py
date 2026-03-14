'''s={"first":"ppap","roll":26,"name":"yashike",26:"nana"}
print(s)
print(s["first"])
for key in s:
    print(key)
print(type(s))
print(len(s))
#print(s[name])# NameError: name 'name' is not defined
#s["name"]: Python looks for the literal text key "name". This works.
#s[name]: (Without quotes) Python thinks name is a variable. It will look for a line of code like name = "some_value"
#  earlier in your script. Since you haven't defined a variable called name, it will throw a NameError.
print(s[26])
name="name"
print(s[name])
#get method to get and print a value
x=s.get("name")
y=s.get("roll")
print(x)
print(y)
#another method of using get method in a dictnorey
print(s.get("name","sheshi"))#returns a value that does not exists in the dict
#d[key]	Error if key not found
#d.get(key)	Returns None
#d.get(key, value)	Returns default value
#get is the best method to get values of a string like if present that key returns non not chooses an error
#in get(,) in this it is like there gives its vlaues from dict not gives out given value'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.keys()
y=car.values()
print(x)
print(type(y))#<class 'dict_values'>
print(car)
car["milage"]=33
print(x)
print(y)
print(car)
#items
print(car.items())#returns in the form of a tuple
#update method is use to add and replcae the elements
#pop. method
car.pop("brand")#removes brand key
car.popitem()#removes the last element
print(car)
x = {}
x=set()#for an empty set
print(type(x))
