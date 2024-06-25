class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]='_'
            else:
                k+=1
        for i in nums:
            if i=='_':
                nums.remove(i)
                nums.append('_')
        print(nums)
        return k
