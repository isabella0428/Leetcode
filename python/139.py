class Solution1:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # include every possible combinations
        # time exceeded
        def generateWord(size, tmp, wordDict):
            nonlocal possible
            length = sum([len(i) for i in tmp])
            if length > size:
                return
            if length == size:
                possible.append("".join(tmp))
                return
            for item in wordDict:
                tmp.append(item)
                generateWord(size, tmp[:], wordDict)
                tmp = tmp[:-1]

        size = len(s)
        tmp = []
        possible = []
        generateWord(size, tmp, wordDict)
        if s in possible:
            return True
        else:
            return False


class Solution2:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dynamic programming
        length = len(s)
        is_breakable = [False for i in range(length + 1)]
        is_breakable[0] = True      # break before the 0th element
        for i in range(1, length + 1):
            for j in range(i):
                if is_breakable[j] and s[j:i] in wordDict:
                    is_breakable[i] = True
        return is_breakable[length]     # break before nth element which doesn't exist ->the end


class Solution3:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # top-down qpproach with memoization

        def word_break(s, dict, start, end, memo):
            if s[start:end + 1] in memo:
                return memo[s[start:end + 1]]
            if s[start:end + 1] in dict:
                memo[s[start:end + 1]] = True
                return True
            for i in range(start, end):
                if s[start:i + 1] in dict and word_break(s, dict, i+1, end, memo):
                    memo[s[start:end + 1]] = True
                    return True
            memo[s[start:end + 1]] = False
            return False
        dict = set(wordDict)
        start = 0
        end = len(s) - 1
        memo = {}
        return word_break(s, dict, start, end, memo)


class Solution4:
    def wordBreak(self, s, wordDict):
        """
        : type s: str
        : type wordDict: dict
        : rtype: bool
        """
        # complete backpack problem
        n = len(s)
        dp = [False for i in range(1 + n)]
        dp[0] = True
        for v in range(1, n + 1):
            for word in wordDict:
                if v >= len(word):
                    dp[v] = dp[v] or (dp[v - len(word)] and s[v - len(word):v] == word)
        return dp[n]


if __name__ == "__main__":
    a = Solution4()
    print(a.wordBreak("applepenapple",
["apple","pen"]))