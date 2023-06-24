def find_max_difference(nums):
    if len(nums) < 2:
        return 0
    
    max_diff = 0
    min_num = nums[0]
    
    for num in nums:
        min_num = min(min_num, num)
        max_diff = max(max_diff, num - min_num)
    
    return max_diff
