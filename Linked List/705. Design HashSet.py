class MyHashSet(object):

    def __init__(self):
            self.my_set = {}
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """        
        self.my_set[key] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.my_set.pop(key,None)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.my_set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)