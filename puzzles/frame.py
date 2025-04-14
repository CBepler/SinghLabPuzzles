'''
Runtime Complexity: Getting the positions that are x is O(mn).
Every element is then looped over for every valid value of k which is up to the min of (n, m) giving this O(min(n,m)*n*m*(work per element))
For each element it must be compared to at most m*n different elements in xPositions.
This gives a runtime of O(m^2n^2 * min(n, m))

Space Complexity: the only added space is xPositions which is O(mn)
'''


def minFrame(filePath):
    dimensions, grid = getData(filePath)
    k = 3
    xPositions = getXPositions(grid)
    while k <= min(dimensions):
        for i in range(dimensions[0] + 1 - k):
            for j in range(dimensions[1] + 1 - k):
                good = True
                for pos in xPositions:
                    if not inSquare(i, j, k, pos):
                        good = False
                        break
                if good : return k
        k += 1
    return 1

def getXPositions(grid):
    xPositions = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'X':
                xPositions.append([row, col])
    return xPositions

def inSquare(row, col, sideLength, xPos):
    xRow = xPos[0]
    xCol = xPos[1]
    if xRow == row or xRow == row + sideLength - 1:  #top or bottom sides of frame
        return xCol >= col and xCol < col + sideLength
    if xCol == col or xCol == col + sideLength - 1:  #left or right sides of frame
        return xRow >= row and xRow < row + sideLength
    return False

def getData(filePath):
    with open(filePath, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    dimensions = lines[0].split(' ')
    dimensions = [int(dim) for dim in dimensions]
    grid = [list(line) for line in lines[1:]]
    return dimensions, grid

if __name__ == "__main__":
    testDir = "puzzles/frameTests/"
    tests = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt"]
    solutions = [3, 1, 1, 1, 3]
    for i in range(len(tests)):
        assert(minFrame(testDir + tests[i]) == solutions[i])
    print("All Tests Passed")