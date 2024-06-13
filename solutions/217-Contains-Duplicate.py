import collections
class Solution(object):
    def containsDuplicate(self, nums):
        freq=collections.Counter(nums)
        for i in freq.values():
            if i>1:
                return True
        return False
