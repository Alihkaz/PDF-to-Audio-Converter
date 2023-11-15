# # importing required modules 

import requests

# from PyPDF2 import PdfReader 

from PyPDF2 import PdfReader

import os


  
# creating a pdf reader object 
reader = PdfReader('uploads/A1_trading_plan.pdf')#upload your pdf and put it here ! 
  
# printing number of pages in the pdf file 
print(len(reader.pages)) 
  
# getting a specific page from the pdf file , in this case its the first page 
page = reader.pages[0] 
  
# extracting text from page 
text = page.extract_text() 
print(text) 


url = "https://open-ai21.p.rapidapi.com/texttospeech"

payload = { "text": text }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": os.environ.get("X-RapidAPI-Key"), #your api key from rapidapi/open-ai21
	"X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())

#go to the link produced in the terminal , there you will find the link to the voice !
# be aware from the bad pdf quality because that will result in errors !
