class Solution:
    def combinationSum3(self, k, n):
        ret = []
        if n > k * 9 or n < k:
            return ret

        def recursive(tmp, idx, k, target):
            if k == 0:
                if target == 0:
                    tmp.sort()
                    if tmp not in ret:
                        ret.append(tmp)
                return
            if k > 9 - idx or target < (idx + 1 + idx + k) * k / 2 or target > (9 + 10 - k) * k / 2:
                return
            for i in range(idx + 1, 10):
                if i not in tmp:
                    tmp.append(i)
                    recursive(tmp[:], i, k - 1, target - i)
                    tmp.pop()

        recursive([], 0, k, n)
        return ret


if __name__ == "__main__":
    a = Solution()
    print(a.combinationSum3(3, 15))