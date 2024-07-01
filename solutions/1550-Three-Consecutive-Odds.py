class Solution(object):
    def threeConsecutiveOdds(self, arr):
        n=len(arr)
        for i in range(n-2):
            c=0
            for j in arr[i:i+3]:
                if j%2==1:
                    c+=1
            if c==3:
                return True
        return False
