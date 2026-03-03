# number game 
# nums = [1,5,233,7]
n1=0
n2=0
for i in range(1,len(nums)):
    #player 1
    if(nums[len(s)-1-i]>nums[i]):
        #take nums[o]
        n1=n1+nums[i-1]
    else:
        n1=n1+nums[len(s)-1-i]
    #player 2
    if(nums[len(s)-1-i]>nums[i]):
        #take nums[o]
        n1=n1+nums[i-1]
    else:
        n1=n1+nums[len(s)-1-i]
