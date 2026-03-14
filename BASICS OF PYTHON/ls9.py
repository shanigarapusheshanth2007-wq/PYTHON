nums = [-1,0,1,2,-1,-4]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        t=-nums[i]-nums[j]
        for k in range(j+1,len(nums)):
            if i!=j and j!=k and k!=i:
                if nums[k]==t:
                    print(i,j,k)
        
