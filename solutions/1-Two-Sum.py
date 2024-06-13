class Solution(object):
    def twoSum(self, nums, target):
        r=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((nums[i]+nums[j])==target and (j!=i)):
                    r.extend([i,j])
                    return r
