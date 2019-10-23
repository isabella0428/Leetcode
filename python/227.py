class Solution:
    def calculate(self, s: str) -> int:
        def getResult(a, b, operator):
            a, b = int(a), int(b)
            if operator == "+":
                return a + b
            if operator == "-":
                return a - b
            if operator == '*':
                return a * b
            if operator == '/':
                return int(a / b)

        stack = []
        prev = ""
        s = s.lstrip(" ")
        s = s.rstrip(" ")
        for item in list(s):
            if item in '+-*/':
                stack.append(prev)
                prev = ""
                stack.append(item)
            else:
                prev += item
        stack.append(prev)

        # first deal with */
        tmp = []
        sign = False
        for item in stack:
            if item in "*/":
                sign = True
                tmp.append(item)
            elif sign:
                op = tmp.pop()
                a = tmp.pop()
                tmp.append(str(getResult(a, item, op)))
                sign = False
            else:
                tmp.append(item)

        # then deal with +-
        tmp2 = []
        sign = False
        for item in tmp:
            if item in "+-":
                sign = True
                tmp2.append(item)
            elif sign:
                op = tmp2.pop()
                a = tmp2.pop()
                tmp2.append(str(getResult(a, item, op)))
                sign = False
            else:
                tmp2.append(item)
        return int(tmp2[-1])


if __name__ == "__main__":
    a = Solution()
    print(a.calculate("3+2*2"))