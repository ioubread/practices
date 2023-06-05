myArray = [89, 34, 67, 90, 12, 56, 80, 120, 6, 250]


def quickSort(inputArray):

    if len(inputArray) > 1:

        less = []
        equal = []
        more = []

        key = inputArray[0]

        for x in inputArray:

            if x < key:
                less.append(x)

            elif x == key:
                equal.append(x)

            elif x > key:
                more.append(x)

        
        return (quickSort(less) + equal + quickSort(more))

    else:
        return inputArray




print(quickSort(myArray))