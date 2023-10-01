class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums[:k]
        self.size = k

        heapq.heapify(self.nums)

        for i in range(k, len(nums)):
            if nums[i] > self.nums[0]:
                heappushpop(self.nums, nums[i])

        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.size:
            heappush(self.nums, val)
        elif(val > self.nums[0]):
            heapreplace(self.nums, val)
        
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)