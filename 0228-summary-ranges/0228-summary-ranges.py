class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        opener, counter = nums[0], nums[0]
        array = []
        i = 1
        string = ''

        while i < len(nums):
            if nums[i] == counter + 1:
                counter = nums[i]
            else:
                if opener != counter:
                    s = str(opener) + '->' + str(counter)
                    array.append(s)
                else: 
                    array.append(str(opener))
                opener, counter = nums[i], nums[i]

            i += 1
            
        if opener != counter:
            s = str(opener) + '->' + str(counter)
            array.append(s)
        else: 
            array.append(str(opener))
        print(array)
        return array

            
