class Solution(object):
    def minMaxGame(self, nums):
        n=len(nums)
        if n>1:
            while True:
                newNums=[]
                n=len(nums)
                for i in range(n//2):
                    if i%2==0:
                        newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                    else:
                        newNums.append(max(nums[2 * i], nums[2 * i + 1]))
                nums= newNums
                if len(nums)==1:
                    break
        return nums[0]
