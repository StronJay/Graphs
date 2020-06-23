class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackAncestralTree(lowerDescendant, higherDescendant, difference):
    while difference > 0:
        difference -= 1
        lowerDescendant = lowerDescendant.ancestor
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant


def twoNumberSum(arr, tSum):
    arr.sort()
    i = 0
    j = len(arr) - 1
    print(i , j, arr)
    while i < j:
        print(i, j)
        cur = arr[i] + arr[j]
        print(cur, arr[i], arr[j])
        if cur > tSum:
            j -= 1
        elif cur < tSum:
            i += 1
        else:
            return [arr[i], arr[j]]
    return []
test = [3, 5, -4, 8, 11, 1, -1, 6]
print(twoNumberSum(test, 10))