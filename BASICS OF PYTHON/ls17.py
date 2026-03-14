nums = [2,3,1,1,4]
s=0
for i in range(len(nums)):
    m=max(nums[i+1:len(nums)-1])
    j=nums.index(m)
    i=i+j
    s+=1
print(s)