class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for tk in tokens:
            if tk in '+-*/':
                second = stack.pop()
                first = stack.pop()
                if tk == '+':
                    stack.append(first + second)
                elif tk == '-':
                    stack.append(first - second)
                elif tk == '*':
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            else:
                stack.append(int(tk))
        return stack[-1]
        