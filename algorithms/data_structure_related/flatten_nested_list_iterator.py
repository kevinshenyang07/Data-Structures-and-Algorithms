# Flatten Nested List Iterator
# NestedInteger has #isInteger, #getInteger, #getList
# key is to push the elements to stack in reverse order,
# then flatten it in #hasNext
class NestedIterator(object):
    def __init__(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.addListToStack(nestedList)

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack and not self.stack[-1].isInteger():
            nestedList = self.stack.pop().getList()
            self.addListToStack(nestedList)
        return self.stack

    def addListToStack(self, nestedList):
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])
