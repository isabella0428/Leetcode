class Solution:
    def wordPattern(self, pattern: str, strs: str) -> bool:
        strs = strs.split(" ")
        dicts = {}
        myset = set()
        if len(strs) == 1:
            return len(pattern) == 1
        if len(strs) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dicts and strs[i] not in myset:
                dicts[pattern[i]] = strs[i]
                myset.add(strs[i])
            elif pattern[i] in dicts and dicts[pattern[i]] == strs[i]:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.wordPattern("abc", "b c a"))