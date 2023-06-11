import PyPDF2
import sys
import os

userInputDesiredScale = 0.6
userInputDesiredScale = input("What scale would you like the height to be? 0.6's the default (Enter blank for default): ")

try:
    userInputDesiredScale = float((userInputDesiredScale).strip())
    
except:
    userInputDesiredScale = 0.6


theFileThatWasDraggedIntoHere = sys.argv[1]
folderName = os.path.dirname(theFileThatWasDraggedIntoHere)

fileName = os.path.basename(theFileThatWasDraggedIntoHere)

fileExtension = (((fileName[::-1]).split("."))[0])[::-1]
rawFileName = (((fileName[::-1]).split("."))[1])[::-1]

resultingName = f"{folderName}\\{rawFileName} (Unsqueezed).{fileExtension}"

pdf = theFileThatWasDraggedIntoHere

pdf = PyPDF2.PdfReader(pdf)

writer = PyPDF2.PdfWriter()


print("\nCtrl+C to cancel program\n")

print(f"Folder: {folderName}\nOriginal File: {fileName}\nResult: {rawFileName} (Unsqueezed).{fileExtension}\nScale desired: {userInputDesiredScale}")

input("\nClick enter to continue...\n")

for i in range(len(pdf.pages)):
    page0 = pdf.pages[i]
    page0.scale(1, userInputDesiredScale)
    writer.add_page(page0)


with open(resultingName, "wb+") as f:
    writer.write(f)

