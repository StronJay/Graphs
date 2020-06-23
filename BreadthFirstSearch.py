class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


    def addChild(self, name):
        self.children.append(Node(name))
        return self


    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array

A = Node("A")
A.addChild("B").addChild("C").addChild("D").addChild("E").addChild("F").addChild("G").addChild("H").addChild("I").addChild("J").addChild("K")
print(A.breadthFirstSearch([]))