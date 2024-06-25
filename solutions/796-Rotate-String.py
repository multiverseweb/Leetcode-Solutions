class Solution(object):
    def rotateString(self, s, goal):
        n=len(s)
        for i in range(0,n):
            temp=s[i+1:n]+s[0:i]+s[i]
            if temp==goal:
                return True
        return False
