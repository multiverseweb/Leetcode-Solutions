class Solution:
    def longestPalindrome(self,s):
        from collections import Counter
        count = Counter(s)
        length = 0
        odd_found = False
        for char, freq in count.items():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True
        if odd_found:
            length += 1
        return length
