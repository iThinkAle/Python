def isNumberIn(sortedListOfNumbers, target):
    low = 0
    high = len(sortedListOfNumbers) - 1
    while low <= high:
        mid = (low + high) // 2
        print("mid " + str(mid))
        midValue = sortedListOfNumbers[mid]
        print("midvalue " + str(midValue))

        if midValue == target:
            return True
        elif midValue < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

sortedNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(isNumberIn(sortedNumbers, 7))
print(isNumberIn(sortedNumbers, 11))
print(isNumberIn(sortedNumbers, 4))
print(isNumberIn(sortedNumbers, -1))

#def isNumberIn(sortedListOfNumbers, target):


