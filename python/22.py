class Solution1:
    def __init__(self):
        self.result = []

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bal = 0     # if bal < 0 and bal !=0 at last returns False
        for i in s:
            if i == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        strs = ""
        self.Recursive(strs, 0, 0, n)
        return self.result

    def Recursive(self, strs, nums, cur,  n):
        if len(strs) == 2*n:
            if self.isValid(strs):
                self.result.append(strs)
                return self.result
            return
        else:
            for j in range(2):
                if j == 0:
                    if cur - nums == n:
                        continue
                    self.Recursive(strs + '(', nums, cur + 1, n)
                else:
                    if cur == 0:
                        continue
                    if nums == n:
                        continue
                    nums += 1
                    self.Recursive(strs + ')', nums, cur + 1, n)


class Solution2:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        def recursive(tmp, left, right):
            nonlocal result
            if left == right == 0:
                result.append(tmp)
                return

            if 0 < left < n + 1:
                recursive(tmp + '(', left - 1, right)

            if right > left:
                recursive(tmp + ')', left, right - 1)

        result = []
        recursive("", n, n)
        return result


if __name__ == "__main__":
    a = Solution2()
    print(a.generateParenthesis(3))