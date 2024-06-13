class Solution(object):
    def isValid(self, s):
        matching_parentheses = {')': '(', '}': '{', ']': '['}
        if len(s)<=1 or len(s)%2!=0 or s[0] in matching_parentheses.keys():
            return False
        stack = []
        a=0
        for char in s:
            if char in matching_parentheses.values():
                stack.append(char)
                a+=1
            elif char in matching_parentheses.keys():
                a-=1
                if stack == [] or matching_parentheses[char] != stack.pop():
                    return False
            else:
                return False
        if a ==0:
            return True
        else:
            return False
