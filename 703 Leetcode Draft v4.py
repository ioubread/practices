# This is a WORK IN PROGRESS

myArray = [5, 10, 15, 20, 25]

userinputkth = int(input("Input K: "))

print(f"Array is: {myArray}")

while True:

    print(f"\n\n")

    toAddToArray = int(input("Add a number: "))

    slicedRn = myArray[-userinputkth:]

    input("About to enter the for i loop")

    for i in range (len(slicedRn)):

        if i < (len(slicedRn) - 1):

            print(f"")

            print(f"Current i: {i}")
            print(f"slicedRn[i] = {slicedRn[i]}")
            print(f"slicedRn[i+1] = {slicedRn[i+1]}")
            print(f"toAddToArray = {toAddToArray}")

            print(f"{i} vs {len(slicedRn) - 1}")

            if i < (len(slicedRn) - 1):

                print(f"The versus thing seems to be left < right, so we'll proceed")

                if slicedRn[i] <= toAddToArray <= slicedRn[i+1]:
                    print(f"So fulfilled criteria")
                    print(f"We're working with this version of slicedRn: {[slicedRn]}")
                    print(f"We're going to put the following together: {slicedRn[1:i]} + {[toAddToArray]} + {slicedRn[i:]}")
                    slicedRn = slicedRn[1:i] + [toAddToArray] + slicedRn[i:]
                    break
                else:
                    print(f"Didn't fulfil criteria, moving next, i + 1")

            else:
                
                print(f"Didn't fulfill the left < right criteria, we're skipping")
                break
    
    print(f"\nkth ({userinputkth}) value of array {slicedRn} is \n{slicedRn[0]}")
    print(f"\nslicedRn array: {slicedRn}")