class Solution:
    def countDigitOne(self, n: int) -> int:
        num, ret = len(str(n)), 0
        i = 1
        while i <= n:
            divider = i * 10
            ret += int(n / divider) * i + min(max(0, n % divider - i + 1), i)
            i *= 10
        return ret


if __name__ == "__main__":
    a = Solution()
    print(a.countDigitOne(13))