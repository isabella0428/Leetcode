from collections import defaultdict


class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # greedy: use frequency of letters to calculate
        # sort the f by start: ensure the left point may be in the former one
        dict = defaultdict(list)
        for i in range(len(S)):
            letter = S[i]
            if not dict[letter]:
                dict[letter] = [i, i]
            else:
                dict[letter][1] = i
        count = list(dict.values())
        count.sort(key=lambda x: x[0])
        part = [[0, 0]]
        end = float('-inf')
        for item in count:
            if item[0] > part[-1][1]:
                part.append(item)
            elif item[1] > part[-1][1]:
                part[-1][1] = item[1]
        ans = []
        for item in part:
            ans.append(item[1] - item[0] + 1)
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.partitionLabels("ababcbacadefegdehijhklij"))