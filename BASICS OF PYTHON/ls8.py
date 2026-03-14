height = [1,1]
a=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        area=abs(i-j)*min(height[i],height[j])
        if a<area:
            a=area
        #print(a)
print(a)