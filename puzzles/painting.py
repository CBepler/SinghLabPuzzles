'''
Runtime Complexity: The first bruteForce pass through the houses costs O(n). 
Calculating the rest of the splits only costs O(1) each making all the rest together O(n).
Finding the minimum element of each array is also O(n)
This makes the total runtime O(n)

Space Complexity: 2 n length arrays are introduced which each hold integers.
This makes the space complexity O(n)
'''


def minPaint(houseOrder):
    size = len(houseOrder)
    whiteFirst = []
    blackFirst = []
    whiteFirst.append(bruteForce(0, ['W', 'B'], houseOrder))
    blackFirst.append(size - whiteFirst[0])
    for i in range(1, size):
        if houseOrder[i - 1] == 'B':
            whiteFirst.append(whiteFirst[i - 1] + 1)
            blackFirst.append(blackFirst[i - 1] - 1)
        elif houseOrder[i - 1] == 'W':
            whiteFirst.append(whiteFirst[i - 1] - 1)
            blackFirst.append(blackFirst[i - 1] + 1)
    return min(min(whiteFirst), min(blackFirst))

def bruteForce(splitIdx, colors, houseOrder):
    numChanges = 0
    for i in range(len(houseOrder)):
        if i < splitIdx:
            if houseOrder[i] == colors[1]:
                numChanges += 1
        else:
            if houseOrder[i] == colors[0]:
                numChanges += 1
    return numChanges

if __name__ == "__main__":
    assert(minPaint("BBBB") == 0)
    assert(minPaint("WWBBB") == 0)
    assert(minPaint("WBBBWWWB") == 2)
    assert(minPaint("WBWBWBWBWBB") == 4)
    assert(minPaint("B") == 0)
    assert(minPaint("WB") == 0)
    assert(minPaint("BW") == 0)
    assert(minPaint("BWBWBWBW") == 3)
    assert(minPaint("WWBBWWBB") == 2)
    print("Passed All Tests")