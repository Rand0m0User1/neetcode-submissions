class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(tokens[i])
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(a - b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                elif tokens[i] == '/':
                    stack.append(int(a / b))

        return stack[0]
                

        