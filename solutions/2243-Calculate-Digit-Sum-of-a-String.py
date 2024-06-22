class Solution(object):
    def digitSum(self, s, k):
        while len(s)> k:
            i=0
            temp=[]
            while i<len(s):
                temp.append(s[i:i+k])
                i+=k
            for j in range(len(temp)):
                sum_digits=0
                for z in temp[j]:
                    sum_digits+=int(z)
                temp[j]=str(sum_digits)
            s=''
            for i in temp:
                s+=i
        return s
