
import os
import PyPDF2
import re


os.chdir('/Users/dmo62/Downloads')
#print(os.getcwd())



pdfFileObj = open('sigma916-919.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


parts = []



for pageNumber in range(pdfReader.getNumPages()):
    page = pdfReader.pages[pageNumber]

    parts = []

    #we make the parts variable a list so that we can use the append funciton and add to the list

    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if y >720:
            parts.append(text)

#in the visitor body function i defined the text matrix as 5, which is the standard, and read that y>720 meant the header,
#so for areas where y>720, i want to append the text in to the empty parts variable. i still have yet to call parts or the visitor body function. 

    page.extract_text(visitor_text=visitor_body)

#this is where the visitor body function actually gets used, but in a specific way
#the pages[].extract_text() has a callable object called visitor_text which is meant to house the visitor_body function. 
#the visitor_text object already has the listed visitor_body variables as attributes, so they do not have be typed in

    text_body = ''.join(parts)

    #we create the text_body variable to house the parts list with the .join function used on it. without the .join funtion, 
    #parts remains a list instead of an easy read text. the '' before is what we want to separate the list items with. 
    #if i put a - in the '', saying i want the list items to be separated by a - , it actually messes me up
    #because i have iso_invoicenum = re.complie(r'\d{9}\D'). where im saying im looking for lines where the line
    #literally begines with 9 digits. the - would disqualify the invoice numbers that i am trying to get. 

    #print(text_body)




    iso_invoicenum = re.compile(r'\d{9}\D')
#  
   

    for line in text_body.split('\n'):
        if iso_invoicenum.match(line):
            invoiceNum1, *otherInfo = line.split()          
            print(invoiceNum1)
            
    

# on invoices with more than one page, the function is returning two "invoiceNum1" values for the second page because on those invoices, 
# the first page has the invoice number only once while on the other pages it has them twice. Unless i put a break, which stops the inside loop
# after the first invoiceNum1 is found
            


    print(pageNumber)
    pageNumber = pageNumber + 1

    
    



