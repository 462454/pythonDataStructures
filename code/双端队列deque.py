'''
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
'''

from pythonds.basic.deque import Deque


def pal_checker(s):
    char_deque = Deque()
    for ch in s:
        char_deque.addRear(ch)
    flag = True
    while char_deque.size() > 1 and flag:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            flag = False
    return flag


def checker(s):
    s_deque = Deque()
    [s_deque.addFront(str_) for str_ in s]
    while not s_deque.isEmpty():
        if s_deque.size() == 1:
            return True
        elif s_deque.removeFront() != s_deque.removeRear():
            return False


print(checker('上海自来水来自海上'))

print(pal_checker('山西运煤车煤运西山'))
print(pal_checker('上海自来水来自海上'))
print(pal_checker('python'))
