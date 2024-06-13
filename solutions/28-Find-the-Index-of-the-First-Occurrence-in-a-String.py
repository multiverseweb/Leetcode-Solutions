class Solution(object):
    def strStr(self, haystack, needle):
        flag=False
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                rtype=i
                if ([k for k in haystack[i:i+len(needle)]] == [j for j in needle]):
                    flag=True
                else:
                    flag=False
            if flag==True:
                return rtype
        return -1       
