class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        myList = []
        
        for num in range(1, n + 1):
            if n % num == 0:
                myList.append(num)

        
        print(myList)
        if k > len(myList):
            return -1

        return myList[k - 1]