class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = list(str(num))
            total = 0
            for item in num:
                total += int(item)
            num = total
        return num


if __name__ == "__main__":
    a = Solution()
    print(a.addDigits(38))

