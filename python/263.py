class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while not num % 5:
            num /= 5
        while not num % 3:
            num /= 3
        while not num % 2:
            num /= 2
        return num == 1


if __name__ == "__main__":
    a = Solution()
    print(a.isUgly(14))