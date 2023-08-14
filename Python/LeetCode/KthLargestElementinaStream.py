# class KthLargest:

#     def __init__(self, k: int, nums):
#         self.nums = sorted(nums)
#         self.k = k

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums = sorted(self.nums)

#         if len(self.nums) >= self.k:
#             return self.nums[-self.k]
#         else:
#             return  self.nums[0]
import heapq

class KthLargest:

    def __init__(self, k: int, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

