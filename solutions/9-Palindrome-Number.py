import math
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        flag=False
        num=str(x)
        length=len(num)
        if length%2==0:
            if (num[0:int(math.floor(length/2))])== (num[-1:int(math.floor(length/2))-1:-1]):
                flag=True
            else:
                flag=False
        else:
            if (num[0:int(math.floor(length/2))])== (num[-1:int(math.floor(length/2)):-1]):
                flag=True
            else:
                flag=False
        return flag