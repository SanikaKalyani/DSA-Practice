#problem : Two sum

class Solution:
    def two_sum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
                
# Test cases:

#1.[2,7,11,15],target=9
#[i,j]=[0,1]

#2.[3,2,4],target=6
#[i,j]=[2,4]

#3.[1,2,3],target=10
#[i,j]=[]