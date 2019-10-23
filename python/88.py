class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        m1 = 0
        n1 = 0
        loc = m
        while n1 <= n - 1:
            if m1 == loc:
                break
            if nums1[m1] < nums2[n1]:
                m1 += 1
                continue
            else:
                nums1.insert(m1, nums2[n1])
                n1 += 1
                loc += 1
                nums1.pop()
        if m1 == loc:
            for i in range(loc, m + n):
                nums1[i] = nums2[n1]
                n1 += 1


if __name__ == "__main__":
    a = Solution()
    nums1 = [0]
    nums2 = [1]
    a.merge(nums1, 0, nums2, 1)
    print(nums1)