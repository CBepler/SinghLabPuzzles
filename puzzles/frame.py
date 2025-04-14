'''
Runtime Complexity: Getting the positions that are x is O(mn).
Making the prefixSum array is also O(mn)
The nested loop is k * m * n * (work per element)
k = min(m, n) making this min(m, n) * m * n * (work per element)
The work per element is simply a call to isValidFrame which is O(1)
The total runtime complexity is O(m * n * min(m, n))

Space Complexity: xPositions and prefixSum are both O(mn) making the total O(mn)
'''


def minFrame(filePath):
    dimensions, grid = getData(filePath)
    n, m = dimensions
    xPositions = getXPositions(grid)
    if not xPositions:
        return 1
    prefixSum = [[0] * (m + 1) for _ in range(n + 1)]
    for x, y in xPositions:
        prefixSum[x + 1][y + 1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefixSum[i][j] += prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1]

    def isValidFrame(row, col, sideLength):
        r2, c2 = row + sideLength - 1, col + sideLength - 1
        if r2 >= n or c2 >= m:
            return False
        fullX = (prefixSum[r2 + 1][c2 + 1]
                   - prefixSum[row][c2 + 1]
                   - prefixSum[r2 + 1][col]
                   + prefixSum[row][col])
        innerX = (prefixSum[r2][c2]
                   - prefixSum[row + 1][c2]
                   - prefixSum[r2][col + 1]
                   + prefixSum[row + 1][col + 1])
        totalXs = fullX - innerX
        expectedXs = len(xPositions)
        return totalXs == expectedXs
    
    for k in range(3, min(n, m) + 1):
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                if isValidFrame(i, j, k):
                    return k
    return 1

def getXPositions(grid):
    return [[row, col] for row in range(len(grid)) for col in range(len(grid[row])) if grid[row][col] == 'X']

def getData(filePath):
    with open(filePath, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    dimensions = list(map(int, lines[0].split()))
    grid = [list(line) for line in lines[1:]]
    return dimensions, grid

if __name__ == "__main__":
    testDir = "puzzles/frameTests/"
    tests = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt", "test6.txt"]
    solutions = [3, 1, 1, 1, 3, 7]
    for i in range(len(tests)):
        assert(minFrame(testDir + tests[i]) == solutions[i])
    print("All Tests Passed")