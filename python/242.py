class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicts = {}
        for item in s:
            dicts[item] = dicts.get(item, 0) + 1
        for i in t:
            if i not in dicts or dicts[i] == 0:
                return False
            dicts[i] = dicts[i] - 1
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.isAnagram("aacc", "ccac"))