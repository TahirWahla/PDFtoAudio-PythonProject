import pyttsx3
import PyPDF2

file=open ("path.pdf",mode="rb")
pdf_reader=PyPDF2.PdfFileReader(file)

pages=pdf_reader.getPage(1)

text=pages.extractText()

melo=pyttsx3.init()
melo.say(text)
melo.runAndWait()