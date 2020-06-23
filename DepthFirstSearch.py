class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


    def addChild(self, name):
        self.children.append(Node(name))
        return self


    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


A = Node("A")
B = Node("B")
A.addChild("B").addChild("C").addChild("D")


print(A.name)
print(A.depthFirstSearch([]))

