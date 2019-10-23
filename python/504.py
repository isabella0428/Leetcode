class Solution:
    def convertToBase7(self, num: 'int') -> 'str':
        h_digit = 1
        s_base = ['-'] if num < 0 else []
        r = num = abs(num)
        while h_digit * 7 <= num:
            h_digit *= 7
        while h_digit >= 1:
            quo, r = divmod(r, h_digit)
            s_base.append(str(int(quo)))
            h_digit /= 7
        return "".join(s_base)


if __name__ == "__main__":
    a = Solution()
    print(a.convertToBase7(-7))