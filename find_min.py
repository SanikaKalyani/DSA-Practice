#problem:find min element in array

def find_min(nums):
    min_value=nums[0]
    for num in nums:
        if nums[num]<min_value:
            min_value=num
    return min_value

#test cases
#1.nums=[1,7,-1]
#min_value[0]=1   nums[1]<min_value  7<1  false  min_value=1
#min_value[1]=1   nums[2]<min_value  -1<1  true  min_value=-1
#min_value=-1
