import hashlib
import random
import os
import xlwt
from datetime import datetime


style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('Technorip')

ws.write(0, 0, "No", style0)
ws.write(0, 1, "Timestamp", style0)
ws.write(0, 2, "Verification code", style0)
ws.write(0, 3, "Verification URL", style0)

r = 1
c = 0

for x in range(1,12):
	word = str(random.random())
	#print(word)
	word1 = word.encode('utf8')
	#print(word1)
	salt = hashlib.sha1(word1).hexdigest()[:10]
	print("count : " + str(x))
	vcode = str(salt)
	vcode = vcode.upper()
	vurl = "http://verify.technorip.com/get/?q=" + vcode
	print("verification code: " + vcode)
	print("verification URL: " + vurl)

	data = 'qrcode "'
	data +=  vurl
	data += '" ./qr/'
	data += vcode
	data += '.png'
	print(data)
	retvalue = os.system(data)
	print(retvalue)
	print(" ")
	ws.write(r, 0, str(x))
	ws.write(r, 1, str(datetime.now()), style1)
	ws.write(r, 2, vcode)
	ws.write(r, 3, vurl)
	r+=1

wb.save('export.xls')
