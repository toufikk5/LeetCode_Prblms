class Solution(object):
    def isValid(self, s):
       stack = []
       matches = {')':'(',']':'[','}':'{'}
       for char in s:
         if char in "([{":
            stack.append(char)
         else:
            if not stack or stack[len(stack)-1]!= matches[char]:
                return False
            stack.pop()
       return len(stack) == 0 

        