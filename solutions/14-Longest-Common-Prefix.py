class Solution(object):
    def longestCommonPrefix(self, strs):
        common=""
        length=len(strs)
        min=len(strs[0])
        for i in range(1,length):
            if len(strs[i])<min:
                min=len(strs[i])
        for i in range(min):
            flag=1
            for j in range(1,length):
                if strs[0][i]==strs[j][i]:
                    flag+=1
            if flag==length:
                common += strs[0][i]
            else:
                break
        return common