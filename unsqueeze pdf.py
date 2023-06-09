import PyPDF2

pdf = "input.pdf"

pdf = PyPDF2.PdfFileReader(pdf)

writer = PyPDF2.PdfFileWriter()

for i in range(len(pdf.pages)):
    page0 = pdf.getPage(i)
    page0.scale(1, 0.6)
    writer.addPage(page0)

with open("output.pdf", "wb+") as f:
    writer.write(f)