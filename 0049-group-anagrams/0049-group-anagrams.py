class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = {}
        
        for s in strs:
            key = list(s)
            key.sort()
            key = ''.join(key)

            if key in hashMap.keys():
                hashMap[key].append(s)

            else:
                hashMap[key] = [s]

        return hashMap.values()