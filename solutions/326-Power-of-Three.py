class Solution(object):
    def isPowerOfThree(self, n):
        if n==1:
            return True
        elif n%3==0:
            c=3
            while c<(3**31):
                if n==c:
                    return True
                if c>n:
                    return False
                c*=3
        else:
            return False
