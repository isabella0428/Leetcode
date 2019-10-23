class Solution1:
    # DFS  Time Exceeded!
    def numDecodings(self, s: 'str') -> 'int':
        def DFS(char, s):
            nonlocal solution
            if int(char[0]) == 0:
                return
            if not 0 < int(char) < 27:
                return
            if not s:
                solution += 1
                return
            DFS(s[0], s[1:])
            if len(s) > 1:
                DFS(s[:2], s[2:])

        solution = 0
        DFS(s[0], s[1:])
        if len(s) > 1:
            DFS(s[:2], s[2:])
        return solution


class Solution2:
    def numDecodings(self, s: 'str') -> 'int':
        if not s:
            return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i != 1 and "09" < s[i - 2: i] < "27":
                dp[i] += dp[i - 2]
        return dp[len(s)]



if __name__ == "__main__":
    a = Solution2()
    print(a.numDecodings("1212"))