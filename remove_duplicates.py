#problam: Remove duplicates

class Solution:
    def removeDuplicates(self,nums):
        if len(nums)==0:
            return 0
        
        i=0

        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
    
    #test cases
    #1.nums=[1,1,2]  i=0
    # nums[0]=1 ,nums[1]=1   same      skip
    # nums[0]=1 ,nums[2]=2   not same  keep  i=0+1=1
    # nums[1]=nums[2]       nums[1]=2
    # nums=[1,2]
