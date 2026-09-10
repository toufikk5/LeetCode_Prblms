class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for c in logs : 
            if c == '../':
                if stack :
                    stack.pop()
            elif c == './':
                pass
            else: 
                    stack.append(c)
        return len(stack)     