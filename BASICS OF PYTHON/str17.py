#this question consist of removig all dashes from the given string
s="2-5g-3-J"
k=2
r=s.replace('-',"")
print(r)
#text = "apple"
# Removes all 'p' characters
#new_text = text.replace("p", "") 
#print(new_text)  # Output: "ale"
n=""
l=len(r)
i=len(r)-1
k=0
while i>=0:
    n=r[i]+n
    k=k+1
    if(k==2 and i!=0):
        n="-"+n
        k=0
    i=i-1
print(n.upper())

