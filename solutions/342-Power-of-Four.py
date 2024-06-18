class Solution(object):
    def isPowerOfFour(self, n):
        if n==1:
            return True
        elif n%4==0:
            c=4
            while c<(4**31):
                if n==c:
                    return True
                if c>n:
                    return False
                c*=4
        else:
            return False
