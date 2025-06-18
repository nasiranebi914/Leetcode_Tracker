# Last updated: 6/17/2025, 10:35:01 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in ["/", "+", "*", "-"]:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a+b)
                if i == "*":
                    stack.append(a*b)
                if i == "-":
                    stack.append(a-b)
                if i == "/":
                    stack.append(int(a/b))

            else:
                stack.append(int(i))
        return stack[0]
        