def minFrame(filePath):
    return 0

if __name__ == "__main__":
    testDir = "frameTests/"
    tests = ["test1.txt", "test2.txt", "test3.txt", "test4.txt"]
    solutions = [3, 1, 1, 1]
    for i in range(len(tests)):
        assert(minFrame(testDir + tests[i]) == solutions[i])
    print("All Tests Passed")