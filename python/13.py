class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum = 0
        dict = {}
        dict["I"] = 1
        dict["V"] = 5
        dict["X"] = 10
        dict["L"] = 50
        dict["C"] = 100
        dict["D"] = 500
        dict["M"] = 1000

        for i in range(len(s)):
            a = s[i]
            if i == len(s) - 1:
                sum = sum + dict[a]
            else:
                if dict[a] >= dict[s[i + 1]]:
                    sum = sum + dict[a]
                else:
                    sum = sum - dict[a]

        return sum


class Solution1(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                'CD': 400, 'CM': 900}

        ret = 0
        for i in range(len(s)):
            char = s[i]
            add = dict[char]
            if i != len(s) - 1:
                if s[i:i + 2] in dict:
                    add *= -1
            ret += add
        return ret


if __name__ == "__main__":
    a = Solution1()
    print(a.romanToInt("IV"))