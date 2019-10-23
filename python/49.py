from collections import defaultdict


class Solution1:
    def __init__(self):
        self.ans = {}

    def groupAnagrams(self, strs):     #Anagrams have same sorted values
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        self.ans = defaultdict(list)
        for i in range(len(strs)):
            self.ans[tuple(sorted(strs[i]))].append(strs[i])
        return list(self.ans.values())


class Solution2:
    def __init__(self):
        self.ans = {}

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        self.ans = defaultdict(list)
        for i in range(len(strs)):
            count = [0] * 26
            for k in strs[i]:
                count[ord(k) - ord('a')] += 1
            self.ans[tuple(count)].append(strs[i])
        return list(self.ans.values())


if __name__ == "__main__":
    a = Solution2()
    print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))






