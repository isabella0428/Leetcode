import operator
import re


class mySolution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def parentheses(num):
            if len(num) == 1:
                ans.append(num[0])
                return

            for i in range(0, len(num) - 2, 2):
                tmp = num[i:i + 3]
                val = ops[tmp[1]](int(tmp[0]), int(tmp[2]))
                tmp = num[:i] + num[i + 3:]
                tmp.insert(i, val)
                parentheses(tmp[:])

        # initialization
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
        num = re.split("[-*+]", input)
        ans = []
        loc = 1
        for item in input:
            if item in "+-*":
                num.insert(loc, item)
                loc += 2

        # recursion
        for i in range(0, len(num) - 2, 2):
            tmp = num[i:i + 3]
            val = ops[tmp[1]](int(tmp[0]), int(tmp[2]))
            tmp = num[:i] + num[i + 3:]
            tmp.insert(i, val)
            parentheses(tmp[:])

        ans.sort()
        return ans


class Solution1:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # divide and conquer
        res = []
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
        if input.isdigit():
            return [int(input)]
        for i in range(len(input)):
            if input[i] in '*-+':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for p in res1:
                    for q in res2:
                        res.append(ops[input[i]](p, q))
        return res


if __name__ == "__main__":
    a = Solution1()
    print(a.diffWaysToCompute("2*3-4*5"))





