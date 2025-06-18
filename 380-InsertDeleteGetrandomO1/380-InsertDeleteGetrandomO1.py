# Last updated: 6/17/2025, 10:34:38 PM
import random
class RandomizedSet(object):

    def __init__(self):
        self.r = set()
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.r:
            self.r.add(val)
            return True
        return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.r:
            self.r.remove(val)
            return True
        return False

        

    def getRandom(self):
        """
        :rtype: int
        """
        random_index = random.choice(list(self.r))
        return random_index
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()