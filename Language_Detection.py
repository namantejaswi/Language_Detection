import numpy
import cv2 as cv
import pytesseract as pyt   
from langdetect import detect
from langdetect import detect_langs
from pytesseract import Output
from pdf2image import convert_from_path
import fitz
import re



pdf_file_path='yolo.pdf'        #file defaulting to same folder

file=fitz.open(pdf_file_path)
open('Abridged.txt', 'w').close() #Deleting the contents of the file so that it is not overwritten multiple times

for pageNUmber, page in enumerate(file.pages(),start=1):
    text_file=page.getText()
    txt=open(f'report_page_{pageNUmber}.txt','a')   # we will be apending to same file
    txt.writelines(text_file)
    print(text_file)
    file1=open("Abridged.txt","a")
    file1.write(text_file)
    file1.close()

lang=(detect(text_file))
confidence=(detect_langs(text_file))  #TO DETERMINE THE CONFIDENCE INTERVAL 
print("The language was",lang)
print("With a probability of",confidence)

# Testing other languages

print(detect("मुझे सोना चाहिए"),)
print(detect("Longue vie à la France"))
print(detect("feliz cumpleaños"))

#Detecting headings and paragraphs 
plain_text = open('Abridged.txt').read()

pattern = re.compile('(?m)^(\d+\.\d+\s[ \w,\-]+)\r?$')

print(pattern.findall(plain_text))
