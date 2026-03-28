#problem:find min element in array

def find_min(nums):
    min_value=nums[0]
    for num in nums:
        if nums[num]<min_value:
            min_value=num
    return min_value