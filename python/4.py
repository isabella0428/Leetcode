class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums2) if len(nums1) > len(nums2) else len(nums1)
        n = len(nums1) if len(nums1) > len(nums2) else len(nums2)

        A = nums2 if len(nums1) > len(nums2) else nums1
        B = nums1 if len(nums1) > len(nums2) else nums2
        i = j = 0

        if A == []:
            if B == []:
                return 0
            elif n % 2 == 1:
                return B[int((n + 1) / 2) -1]
            else:
                return int(B[int(n / 2) - 1] + B[int (n / 2)]) / 2

        while 1:
            j = int((m + n + 1) / 2) - i
            if i < m and B[j - 1] > A[i]:
                i = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                i = i - 1

            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                else:
                    if i == m:
                        min_of_right = B[j]
                    elif j == n:
                        min_of_right = A[i]
                    else:
                        min_of_right = min(A[i], B[j])

                return (min_of_right + max_of_left) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        m, n = len(nums1), len(nums2)
        if (m + n) % 2:
            loc1 = loc2 = int((m + n) / 2) + 1
        else:
            loc1 = int((m + n) / 2)
            loc2 = loc1 + 1
        s1, s2 = 0, 0
        num = [None for i in range(m + n)]
        for i in range(loc2):
            term1 = nums1[s1] if s1 < len(nums1) else float('inf')
            term2 = nums2[s2] if s2 < len(nums2) else float('inf')
            if term1 < term2:
                num[i] = term1
                s1 += 1
            else:
                num[i] = term2
                s2 += 1
        return (num[loc1 - 1] + num[loc2 - 1]) / 2


if __name__ == "__main__":
    a = Solution2()
    print(a.findMedianSortedArrays([1], [2,3,4]))


