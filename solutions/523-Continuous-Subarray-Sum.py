class Solution(object):
    def checkSubarraySum(self, nums, k):
        if not nums or len(nums) < 2:
            return None
        r = {0: -1}
        s = 0
        for i, num in enumerate(nums):
            s += num
            a = s % k
            if a in r:
                if i - r[a] > 1:
                    return nums[r[a] + 1:i + 1]
            else:
                r[a] = i
        return False