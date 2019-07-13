class SuperList():
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state=[]):
        self._data = initial_state
        self._calc_length()
        # we added code below this comment
    def __repr__(self):
        string_representation = str(self._data)
        return string_representation
        # we added code above this comment
    def _calc_length(self):
        length = 0
        for item in self._data:
            length +=1
        self.length = length
    def append(self, new_item):
        self._data = self._data + [new_item]
        
        

mylist = SuperList([1,2,3,4,5])
print(mylist.length)
mylist.append(6)
print(mylist)