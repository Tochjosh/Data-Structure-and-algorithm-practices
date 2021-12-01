import random


# To create a custom iterable ADT, first we create the class of the ADT
class Bag:
    def __init__(self):
        self._theItems = list()  # initiate an empty list to store the collection

    def __len__(self):
        return len(self._theItems)  # function that gets the length of the container

    def __contains__(self, item):
        return item in self._theItems

    def add(self, item):
        self._theItems.append(item)

    def remove(self, item):
        assert item in self._theItems, 'The item must be in the list'
        ind = self._theItems.index(item)
        return self._theItems.pop(ind)

    def grabItem(self):
        length = int(len(self._theItems))
        if len == 0:
            return None

        if length == 1:
            return self._theItems[0]

        randInd = random.randint(0, (length - 1))
        return self._theItems.pop(randInd)

    def numItem(self, item):
        num = self._theItems.count(item)
        return num

    def __iter__(self):
        return _BagIterator(self._theItems)  # this is implemented abstracted in the class below


class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration


class ClickCounter:
    def __init__(self):
        self.count = 0

    def push(self):
        self.count += 1
        print(self.count)

    def reset(self):
        self.count = 0
        print(self.count)


counter = ClickCounter()

counter.push()
counter.push()
counter.push()
counter.push()
counter.reset()
