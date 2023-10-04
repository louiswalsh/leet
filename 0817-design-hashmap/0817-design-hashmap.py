class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.values[i] = value
                return    

        self.keys.append(key)
        self.values.append(value)
        return

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.values[i]     

        return -1   

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                del self.values[i]
                del self.keys[i]
                break   


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)