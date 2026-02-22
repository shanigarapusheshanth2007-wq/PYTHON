#string format and its syntax
a,b=10,20
c=a+b
#display as a is 10 b is 20 then c is 30
print('A is {0} and B is {1} then c is {2}'.format(a,b,c))#this is the structre to print a statment in python
#arthemetic
'''
+ - * / % ** exponent operator 2**10 means here 2 power 10 this is astic // floor divison operator
9//2 is 4 not gives 4.5
comparison operators
== check if they are equal
!=
>
<
>=
<=
assignment operators
=
+=
-=
*=
/=
%=
**=
//=
c%=a
is c=c%a
bitwise operators
&
|
^
~
<<
>>
logical operators
a=T b=T
and
or
not
'''
name = "sheshi"
gpa,age= 5,30
a=[1,2,3,"yashika",[1,2,4]]
print(a)
a[3]="nananan"
print(a[1])
print(a[1:4])
print(a[-1])
print(a[-1:-6:-1])
print(a[::-1])
a[-1][2]=100
print(a)
#tuplets
print(format("",'-<30'))
s=(1,'a',"sheshi",[1,2,3])
print(s)
#s[0]=2 we cant use this beacause
print(s)
s[-1][0]=99
print(s)