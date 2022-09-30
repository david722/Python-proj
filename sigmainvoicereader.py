import os
import PyPDF2
import re

os.chdir('/Users/dmo62/Downloads')
#print(os.getcwd())

invoiceNumbers = []
invoicelist = []

pdfFileObj = open('', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

parts = []

for pageNumber in range(pdfReader.getNumPages()):
    page = pdfReader.pages[pageNumber]

    parts = []

    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if y >720:
            parts.append(text)
    page.extract_text(visitor_text=visitor_body)

    text_body = ''.join(parts)

    iso_invoicenum = re.compile(r'\d{9}\D')

    for line in text_body.split('\n'):
        
        if iso_invoicenum.match(line):
            invoiceNum, *otherInfo = line.split()   
    invoiceNumbers.append(invoiceNum)

for pageNumber, invoiceNum in enumerate(invoiceNumbers, start = 1):
    if invoiceNum not in invoicelist:
        invoicelist.append(invoiceNum)
    else:
        continue
    print(pageNumber, invoiceNum)


    
    



