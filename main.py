import pyttsx3
import PyPDF2
book = open('UPSC Q Paper.pdf', 'rb')    #Write Your Pdf file name in the quotes 
pdfReader = PyPDF2.PdfFileReader(book)   #To Read a pdf file
pages = pdfReader.numPages               #To get the number of pages in the pdf
print(pages) 
speaker = pyttsx3.init()                 #To initialize the pyttsx3
for num in range(7, pages): 
    page = pdfReader.getPage(num)        #To get the page to be read
    text = page.extractText()            #For extraction of text from the page
    speaker.say(text)
    speaker.runAndWait()
