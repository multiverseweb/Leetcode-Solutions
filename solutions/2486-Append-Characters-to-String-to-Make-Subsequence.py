class Solution(object):
    def appendCharacters(self, s, t):
        i, j = 0, 0
        a=len(s)
        b=len(t)
        while i < a and j < b:
            if s[i] == t[j]:
                j += 1
            i += 1
        return b - j
