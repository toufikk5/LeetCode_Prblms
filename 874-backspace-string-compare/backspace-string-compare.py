class Solution(object):
    def backspaceCompare(self, s, t):
       def build(string):
        stack = []
        for char in string:
            if char!= '#':
                stack.append(char)
            else :
                if stack:
                 stack.pop()
        return stack
       return build(s) == build(t)