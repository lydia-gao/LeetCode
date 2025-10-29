class RandomizedSet(object):

    def __init__(self):
        self.list = []
        self.pos = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        # index of the value we're removing
        idx = self.pos[val]

        # value at the end of the list
        last_val = self.list[-1]

        # move last_val into idx
        self.list[idx] = last_val
        self.pos[last_val] = idx

        # remove last element from list
        self.list.pop()

        # delete val from map
        del self.pos[val]

        return True


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()