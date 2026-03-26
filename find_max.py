#problem:find max element in array

def find_max(nums):
    max_value=nums[0]
    for num in nums:
        if nums[num]>max_value:
            max_value=num
    return max_value