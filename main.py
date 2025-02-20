import pyttsx3
import PyPDF2
book = open('Dummy.pdf', 'rb')    #Write Your Pdf file name in the quotes 
pdfReader = PyPDF2.PdfReader(book)   #To Read a pdf file
pages = len(pdfReader.pages)              #To get the number of pages in the pdf
print(pages) 
speaker = pyttsx3.init()                 #To initialize the pyttsx3
for num in range(0, pages): 
    page = pdfReader.pages[num]        #To get the page to be read
    text = page.extract_text()            #For extraction of text from the page
    speaker.say(text)
    speaker.runAndWait()
