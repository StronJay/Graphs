test = [3, 5, 6, -5, -2, -5, -28, -2, -1, 2, -6, 1, 1, 2, -5, 2]
def oneCycleArray(array):
    print(array)
    numberOfElementsVisitedInTheArray = 0
    currentIdx = 0
    while numberOfElementsVisitedInTheArray < len(array):
        #print("currIdx:", currentIdx, "ElementsVisited:", numberOfElementsVisitedInTheArray)
        if numberOfElementsVisitedInTheArray > 0 and currentIdx == 0:
            return False
        numberOfElementsVisitedInTheArray += 1
        currentIdx = getNextIdx(currentIdx, array)
        print(currentIdx)
    return currentIdx == 0


def getNextIdx(i, array):
    jump = array[i]
    nextIdx = (i + jump) % len(array)
    print("i", i, "+", "jump", jump, "% len(array)", len(array), "=", nextIdx)
    return nextIdx

print(oneCycleArray(test))