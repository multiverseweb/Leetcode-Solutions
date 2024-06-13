class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        elif n%2==0:
            c=2
            while c<(2**31):
                if n==c:
                    return True
                if c>n:
                    return False
                c*=2
        else:
            return False
