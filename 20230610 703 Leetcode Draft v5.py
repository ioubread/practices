# This is a WORK IN PROGRESS

myArray = []

while True:
    toAddThisToInitialArray = (input(f"Add a number to the initial array: "))

    if toAddThisToInitialArray == "":
        break
    else:
        myArray.append(int(toAddThisToInitialArray))


myArray.sort()

userinputkth = int(input("Input K: "))

slicedRn = myArray[-userinputkth:]

print(f"Array is: {myArray}")
print(f"Array is: {slicedRn}")

while True:

    print(f"\n\n")

    toAddToArray = int(input("Add a number: "))

    if toAddToArray >= slicedRn[-1]:
        slicedRn = slicedRn[1:] + [toAddToArray]
    
    else:

        for i in range (len(slicedRn)):
            if i < len(slicedRn)-1:

                print(f"\ni: {i}")
                itemA = slicedRn[-(i+1)]
                itemB = slicedRn[-(i+2)]
                print(f"{itemB} <= {toAddToArray} <= {itemA}?")
                if itemA >= toAddToArray >= itemB:
                    slicedRn = slicedRn[1:((len(slicedRn)-1)-i)] + [toAddToArray] + slicedRn[-(i+1):]
                    break
                else:
                    pass
            else:
                break

    print(f"\n\nFirst number of {slicedRn}: {slicedRn[0]}")

