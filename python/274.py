class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        n = len(citations)
        h = []
        for i in range(n):
            if i + 1 <= citations[i]:
                h.append(i + 1)
        return max(h) if h else 0


if __name__ == "__main__":
    a = Solution()
    print(a.hIndex([0]))