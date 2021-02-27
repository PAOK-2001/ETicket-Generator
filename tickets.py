
# Import library
import gspread
import qrcode
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image


scope = [
         'https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive',
        ]

credentials = ServiceAccountCredentials.from_json_keyfile_name('Winter Ball-8cef2ea3f383.json', scope)
#Credentials of the reference spreadsheet ie Ticket database. Obtained with google API

gc = gspread.authorize(credentials)

sheet = gc.open("Boletos Winterball").sheet1

data = sheet.get_all_values()

template = Image.open('Template.png') #Ticket design template, should be incluede in code´s folder
template_width, template_height = template.size

#Read data from spreadsheet
for idx, row in enumerate(data):
    if idx ==0 or row[1]=="":
        continue

    ticket_code = row[1] + row[0]   #Create ticket ID, in this case name + number
    code = qrcode.make(ticket_code)
    code_width, code_height = code.size
    template.paste(code, (int(template_width/2 - code_width/2), 668))
    template.save(ticket_code + ".png") #Create Ticket




