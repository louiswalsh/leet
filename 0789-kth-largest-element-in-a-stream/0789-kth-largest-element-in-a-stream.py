class KthLargest(object):
    kthLargest = None
    k = None
    nums = []

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.recalculate()
        
        return self.kthLargest
        
    def recalculate(self):
        self.nums.sort()
        self.kthLargest = self.nums[-self.k]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)