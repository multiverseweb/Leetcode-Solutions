import collections
class Solution(object):
    def majorityElement(self, nums):
        freq=collections.Counter(nums)
        m=max(freq.values())
        return list(freq.keys())[list(freq.values()).index(m)]
