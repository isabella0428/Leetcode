class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ans = []
        d.sort(key=lambda x : len(x))
        d = d[::-1]
        for item in d:
            s_start, item_start = 0, 0
            while s_start < len(s) and item_start < len(item):
                if s[s_start] == item[item_start]:
                    item_start += 1
                    if item_start == len(item):
                        ans.append(item)
                        if len(ans) == 1:
                            continue
                        if len(ans[-1]) < len(ans[-2]):
                            ans = ans[:-1]
                            ans.sort()
                            return ans[0]
                s_start += 1
        ans.sort()
        return ans[0] if ans else ""


if __name__ == "__main__":
    a = Solution()
    print(a.findLongestWord("foobarfoobar",["foo","bar"]))

