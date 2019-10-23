class Solution1:
    def __init__(self):
        self.result = []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        strs = []
        s = []
        dict = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'],
               6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
        for i in digits:
            s.append(dict[int(i)])
        length = len(s)
        self.Recursive(s, 0, length)
        return self.result

    def Recursive(self, s, i, length, ans=""):
        if i == length:
            self.result.append(ans)
        else:
            for p in s[i]:
                ans += p
                self.Recursive(s, i + 1, length, ans)
                ans = ans[:-1]


class Solution2:
    def __init__(self):
        self.result = []

    def digitLetter(self, digit):
        if digit == '1':
            return []
        elif digit == '2':
            return ['a', 'b', 'c']
        elif digit == '3':
            return ['d', 'e', 'f']
        elif digit == '4':
            return ['g', 'h', 'i']
        elif digit == '5':
            return ['j', 'k', 'l']
        elif digit == '6':
            return ['m', 'n', 'o']
        elif digit == '7':
            return ['p', 'q', 'r', 's']
        elif digit == '8':
            return ['t', 'u', 'v']
        else:
            return ['w', 'x', 'y', 'z']

    def recursive(self, tmp, digits):
        if not digits:
            self.result.append(tmp)
            return
        for char in self.digitLetter(digits[0]):
            self.recursive(tmp + char, digits[1:])

    def letterCombinations(self, digits: 'str') -> 'List[str]':
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.recursive("", digits)
        return self.result


if __name__ == "__main__":
    a = Solution2()
    print(a.letterCombinations("23"))







