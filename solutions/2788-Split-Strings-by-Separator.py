class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        ans=[]
        for i in words:
            temp2=[]
            temp=i.split(separator)
            for j in temp:
                if j!='':
                    temp2.append(j)
            ans.extend(temp2)
        return ans
