import os
import PyPDF2
import re

os.chdir('/Users/dmo62/Downloads')
#print(os.getcwd())

invoiceNumbers = []
invoicelistdict = {}

pdfFileObj = open('sigma913-915.pdf', 'rb')
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

pageNumberList = []

for pageNumber, invoiceNum in enumerate(invoiceNumbers, start = 1):
    pageNumberList.append(pageNumber)

# print(pageNumberList)
# print(invoiceNumbers)

d = dict(zip(pageNumberList, invoiceNumbers))

#print(d)

temp = []
res = dict()
for key, val in d.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)


# print(invoicelist)

# def Convert(a):
#     it = iter(a)
#     res_dct = dict(zip(it, it))
#     return res_dct
         
# # Driver code
# invoiceNumbers = ['a', 1, 'b', 2, 'c', 3]
# print(Convert(lst))


    


    
    



