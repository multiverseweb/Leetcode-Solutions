class Solution:
    def minIncrementForUnique(self,nums):
        nums.sort()
        m=0
        for i in range(1, len(nums)):
            if nums[i]<=nums[i-1]:
                increment=nums[i-1] - nums[i]+1
                m+=increment
                nums[i] = nums[i-1]+1
        return m
