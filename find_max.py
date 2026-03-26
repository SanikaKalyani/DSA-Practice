#problem:find max element in array

def find_max(nums):
    max_value=nums[0]
    for num in nums:
        if nums[num]>max_value:
            max_value=num
    return max_value

#test cases
#1.nums=[1,7,3]
#max_value[0]=1   nums[1]>max_value  7>1  true  max_value=7
#max_value[1]=7   nums[2]>max_value  3>7  false max_value=7
#max_value=7
