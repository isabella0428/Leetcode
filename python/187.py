from collections import defaultdict


class Solution1(object):
    # Time Limit Exceeded!
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n <= 10:
            return []
        seen, ret = [], []
        for i in range(9, n):
            if s[i - 9:i + 1] in seen and s[i - 9:i + 1] not in ret:
                ret.append(s[i - 9:i + 1])
            else:
                seen.append(s[i - 9:i + 1])
        return ret


class Solution2(object):
    # Use dict for hashset(Ologn)
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n <= 10:
            return []
        seen = defaultdict(int)
        for i in range(9, n):
            seen[s[i - 9: i + 1]] += 1
        return [key for key, val in seen.items() if val > 1]


class Solution3(object):
    # Optimized!
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n <= 10:
            return []
        seen, ret = set(), set()
        for i in range(9, n):
            if s[i - 9:i + 1] in seen:
                ret.add(s[i - 9:i + 1])
            else:
                seen.add(s[i - 9:i + 1])
        return list(ret)


if __name__ == "__main__":
    a = Solution3()
    print(a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))