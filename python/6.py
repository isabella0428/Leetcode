class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        Rows = []
        for i in range(numRows):
            Rows.append([])

        for j in range(len(s)):
            if int(j / (numRows - 1)) % 2 == 0 :
                Rows[j % (numRows - 1)].append(s[j])
            else:
                Rows[numRows - 1 - j % (numRows - 1)].append(s[j])

        string = ""
        for i in range(numRows):
            for j in Rows[i]:
                string = string + j

        return string


if __name__ == "__main__":
    a = Solution()
    print(a.convert("AB",1))
