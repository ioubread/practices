# This is a WORK IN PROGRESS
"""
Input K: 2
Array is: [5, 10, 15, 20, 25]
Add a number: 17
kth value of array [20, 25] is 
20
Add a number: 13
kth value of array [20, 25] is 
20
Add a number: 23
kth value of array [23, 20, 25] is 
23
Add a number: 24
kth value of array [24, 20, 25] is 
24
"""


myArray = [5, 10, 15, 20, 25]

userinputkth = int(input("Input K: "))

print(f"Array is: {myArray}")

while True:

    toAddToArray = int(input("Add a number: "))

    slicedRn = myArray[-userinputkth:]

    for i in range (len(slicedRn)):

        if slicedRn[i] <= toAddToArray <= slicedRn[i+1]:
            slicedRn = slicedRn[1:i] + [toAddToArray] + slicedRn[i:]
            break
    
    print(f"kth value of array {slicedRn} is \n{slicedRn[0]}")
