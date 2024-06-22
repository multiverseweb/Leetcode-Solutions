import collections
class Solution(object):
    def firstUniqChar(self, s):
        d=collections.Counter(s)
        pos=-1
        for i in s:
            pos+=1
            if d[i]==1:
                return pos
        if pos==len(s)-1:
            return -1
