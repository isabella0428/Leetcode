import operator
class Solution1:
    # Dynamic Programming
    def findLongestChain(self, pairs: 'List[List[int]]') -> 'int':
        pairs = sorted(pairs, key = lambda x: x[0])
        n = len(pairs)
        if n == 0 or n == 1:
            return n
        memo = [1 for i in range(n + 1)]
        for i in range(2, 1 + n):
            for j in range(i - 1):
                if pairs[i - 1][0] > pairs[j][1]:
                    memo[i] = max(memo[i], 1 + memo[j + 1])
        return max(memo)


class Solution2:
    # Greedy
    # get the item with the smallest second value
    def findLongestChain(self, pairs: 'List[List[int]]') -> 'int':
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans


if __name__ == "__main__":
    a = Solution2()
    print(a.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]))