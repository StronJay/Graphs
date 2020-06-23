test = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]


def riverLengths(chart):
    lengths = []
    visited = [[False for x in y] for y in chart]
    for i in range(len(visited)):
        print(visited[i], chart[i], i)
    for i in range(len(chart)):
        for j in range(len(chart[i])):
            if visited[i][j]:
                continue
            findlengths(i, j, chart, visited, lengths)
    return lengths


def findlengths(i, j, chart, visited, lengths):
    river = 0
    uncharted  = [[i, j]]
    print(uncharted)
    while len(uncharted):
        place = uncharted.pop()
        i = place[0]
        j = place[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if chart[i][j] == 0:
            continue
        river += 1
        notExplored = getUnexplored(i, j, chart, visited)
        for land in notExplored:
            uncharted.append(land)
    if river > 0:
        lengths.append(river)


def getUnexplored(i, j, chart, visited):
    unexplored = []
    if i > 0 and not visited[i - 1][j]:
        unexplored.append([i - 1, j])
    if i < len(chart) - 1 and not visited[i + 1][j]:
        unexplored.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unexplored.append([i, j - 1])
    if j < len(chart[0]) - 1 and not visited[i][j + 1]:
        unexplored.append([i, j + 1])
    return unexplored


print(riverLengths(test))
