nums = [-1,2,1,-4]
target = 1
c=100
l=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            s=nums[i]+nums[j]+nums[k]
            d=abs(s-target)
            if c>d:
                c=d
                
                l=[nums[i],nums[j],nums[k]]
print(l)