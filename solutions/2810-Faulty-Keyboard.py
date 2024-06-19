class Solution:
    def finalString(self,s):
        temp=""
        for i in s:
            if i=='i':
                temp=temp[::-1]
            else:
                temp+=i
        return temp
