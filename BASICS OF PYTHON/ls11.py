arr = [1,2,3,7,5]
n=max(arr)
print(n)
j=arr.index(n)
temp=arr[j-1]
arr[j-1]=arr[j]
arr[j]=temp
print(arr)
