import math
class Solution(object):
    def isHappy(self, n):
        temp=n
        num=str(n)
        c=0
        while True:
            s=0
            c+=1
            for i in num:
                s+=int(i)**2
                num=str(s)
            if s==1:
                return True
            if c==20:
                break
        return False
