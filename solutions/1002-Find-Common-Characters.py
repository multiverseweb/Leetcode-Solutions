class Solution(object):
    def commonChars(self, words):
        n=len(words)
        if n==0:
            return words
        r=[]
        if n==1:
            for i in words[0]:
                r.append(i)
            return r
        m=words[0]
        for i in words:
            if len(i)<len(m):
                m=i
        for i in m:
            c=0
            for j in range(n):
                if i in words[j]:
                    c+=1
            if c==n:
                for k in range(n):
                    words[k]=words[k].replace(i,"",1)
                r.append(i)
        return r
