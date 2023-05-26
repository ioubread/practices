theArray = [4, 4, 5, 5,  9, 10, 8, 2, 3]

theArray.sort()

slicedArray = theArray[-3:]

kth, kplusone, kplustwo = slicedArray

newnumber = int(input("Enter new number: "))

if newnumber > kth and newnumber < kplusone:
    kth = newnumber

elif newnumber > kplusone and newnumber < kplustwo:
    kth = kplusone
    kplusone = newnumber

elif newnumber > kplustwo:
    kth = kplusone
    kplusone = kplustwo
    kplustwo = newnumber
