myArray = [124,234,32,154,52,4321,32,132,32,4,1,421,4,6,345,234,2]


def mergeSort(inputArray):

    # This function only matters if the size is more than 1, otherwise it's already sorted

    if len(inputArray) > 1:

        # print(len(inputArray))

        leftArray = inputArray[:len(inputArray)//2]
        rightArray = inputArray[len(inputArray)//2:]

        # print(leftArray)
        # print(rightArray)

        # print(len(leftArray))

        mergeSort(leftArray)
        mergeSort(rightArray)


        i = 0
        j = 0
        k = 0

        while (i < len(leftArray) and j < len(rightArray)):

            if leftArray[i] < rightArray[j]:
                inputArray[k] = leftArray[i]
                i += 1
                k += 1
            
            else:
                inputArray[k] = rightArray[j]
                j += 1
                k += 1
        
        while i < len(leftArray):

            inputArray[k] = leftArray[i]
            i += 1
            k += 1
        
        while j < len(rightArray):

            inputArray[k] = rightArray[j]
            j += 1
            k += 1

    return inputArray



        

print(mergeSort(myArray))