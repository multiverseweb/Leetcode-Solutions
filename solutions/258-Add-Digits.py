class Solution(object):
    def addDigits(self, num):
        n=len(str(num))
        if n<2:
            return num
        num=str(num)
        while n>1:
            temp=0
            for i in range(n):
                temp+=int(num[i])
            num=str(temp)
            n=len(num)
        return int(num)
