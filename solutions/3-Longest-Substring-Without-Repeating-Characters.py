class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s=="":
            return 0
        arr=[]
        c=0
        n=len(s)
        while c!=n:
            temp=""
            for i in range(c,n):
                if s[i] not in temp:
                    temp+=s[i]
                else:
                    break
            arr.append(temp)
            c+=1
        ans=arr[0]
        for i in arr:
            if len(i)>len(ans):
                ans=i
        return len(ans)