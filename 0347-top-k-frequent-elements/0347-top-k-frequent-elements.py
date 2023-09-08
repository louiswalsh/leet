import operator

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numsSet = {}
        answers = [None] * k

        for idx, num in enumerate(nums):
            if num in numsSet.keys():
                numsSet[num] += 1
            else: 
                numsSet[num] = 1

        sortedDict = sorted(numsSet.items(), key=lambda x:x[1])
        sortedDict.reverse()

        for i in range(0, k):
            answers[i] = sortedDict[i][0]
            

        return answers