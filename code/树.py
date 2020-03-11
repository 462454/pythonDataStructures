myTree = ['a',
          ['b',
           ['d', [], []],
           ['e', [], []]],
          ['c',
           ['f', [], []],
           []
           ]
          ]

print('左树：', myTree[1])
print('根节点：', myTree[0])
print("右树：", myTree[2])


# 抽象数据类型  ADT或者节点表示方式


class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = Node(elem)
        if not self.root:
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if not cur.lchild:
                    cur.lchild = node
                    return
                elif not cur.rchild:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
