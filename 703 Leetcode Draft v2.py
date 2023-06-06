myArray = [5, 10, 15, 20, 25]

userinputkth = int(input("Input K: "))

print(f"Array is: {myArray}")

while True:
    print(f"kth value of array {myArray} is: {(myArray[-userinputkth])}")
    
    toAddToArray = int(input("Add a number: "))

    myArray.append(toAddToArray)
    myArray.sort()