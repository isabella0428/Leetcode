class Solution1(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words == []:
            return []
        num = len(words)
        word_num = len(words[0])
        index = []
        target = []
        ans = []
        for i in range(len(s) - num * word_num + 1):
            target = []
            for j in range(i, i + num * word_num, word_num):
                target.append(s[j: j + word_num])
            Flag = False
            for item in words:
                if item in target:
                    target.remove(item)
                    continue
                else:
                    Flag = True
                    break
            if not Flag:
                ans.append(i)
        return ans


class Solution2:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        def check(s, loc, dicts, count, w_length):
            already = {}
            for i in range(loc, loc + (count - 1) * w_length + 1, w_length):
                word = s[i:i + w_length]
                if word in dicts and already.get(word, 0) != dicts[word]:
                    already[word] = already.get(word, 0) + 1
                    continue
                return False
            return True

        if not s or not words:
            return []
        w_length, dicts = len(words[0]), {}
        count, ret = 0, []
        for word in words:
            dicts[word] = dicts.get(word, 0) + 1
            count += 1
        for i in range(len(s) - count * w_length + 1):
            if check(s, i, dicts, count, w_length):
                ret.append(i)
        return ret


if __name__ == "__main__":
    a = Solution2()
    print(a.findSubstring("barfoofoobarthefoobarman",
["bar","foo","the"]))