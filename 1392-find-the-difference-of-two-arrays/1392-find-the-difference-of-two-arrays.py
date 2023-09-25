class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        stk = []

        for n in set1:
            if n in set2:
                stk.append(n)


        for n in stk:
            set1.remove(n)
            set2.remove(n)


        return [set1, set2]

        