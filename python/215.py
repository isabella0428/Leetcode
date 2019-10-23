import random
class Solution1(object):
    # nlog(n)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def perlocate(nums, loc, size):
            tmp = nums[loc]
            while loc * 2 + 1 < size:
                child = loc * 2 + 1
                if child + 1 < size:
                    if nums[child + 1] > nums[child]:
                        child += 1
                if nums[child] > tmp:
                    nums[loc] = nums[child]
                    loc = child
                else:
                    break
            nums[loc] = tmp

        size = len(nums)
        for i in range(int((size - 1) / 2), -1, -1):
            perlocate(nums, i, size)

        for i in range(size - 1, max(size - k - 1, -1), -1):
            nums[0], nums[i] = nums[i], nums[0]
            perlocate(nums, 0, i)
        return nums[-k]


class Solution2:
    # nlog(k)   keep a heap with k elements
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # min-heap
        def perlocate(heap, hole, size):
            tmp = heap[hole]
            while 2 * hole + 1 < size:
                child = 2 * hole + 1
                if child + 1 < size and heap[child + 1] < heap[child]:
                    child += 1
                if heap[child] < tmp:
                    heap[hole] = heap[child]
                    hole = child
                else:
                    break
            heap[hole] = tmp

        num = 0
        heap = nums[:k]
        for i in range(int(k / 2), -1, -1):
            perlocate(heap, i, k)

        for item in nums[k:]:
            if item < heap[0]:
                continue
            heap[0] = item
            perlocate(heap, 0, k)
        return heap[0]

class Solution3:
    # Quicksort
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            #moves pivot to the end
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[store_index], nums[right] = nums[right], nums[store_index]
            return store_index

        def select(nums, left, right, k_smallest):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            index = partition(left, right, pivot_index)
            if index == k_smallest:
                return nums[index]
            if index < k_smallest:
                return select(nums, index + 1, right, k_smallest)
            else:
                return select(nums, left, index - 1, k_smallest)

        return select(nums, 0, len(nums) - 1, len(nums) - k)


class Solution4:
    def findKthLargest(self, nums, k):
        def perlocate(hole, nums, size):
            tmp = nums[hole]
            while 2 * hole + 1 <= size:
                child = 2 * hole + 1
                if child <= size - 1 and nums[child + 1] > nums[child]:
                    child += 1
                if nums[child] > tmp:
                    nums[hole] = nums[child]
                    hole = child
                else:
                    break
            nums[hole] = tmp

        def buildHeap(nums, k):
            heap = nums
            size = len(heap) - 1
            for i in range(int(size / 2), -1, -1):
                perlocate(i, heap, size)

            for i in range(k):
                heap[0], heap[size - i] = heap[size - i], heap[0]
                perlocate(0, heap, size - i - 1)
            return nums[-k]

        return buildHeap(nums, k)


if __name__ == "__main__":
    a = Solution4()
    print(a.findKthLargest([3,2,3,1,2,4,5,5,6], 1))