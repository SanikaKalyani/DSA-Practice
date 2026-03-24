#problem : contains duplicate

class Solution:
    def containsduplicate(self,nums):
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
    
#Test cases

#1.nums=[1,1,0,6] 1==1 duplicate found      True
#2.nums=[1,2,3,4]      duplicate not found  false
