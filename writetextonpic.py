# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw,ImageFont
from xlrd import open_workbook
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")
print today
filename = '磁易购【服务需求对接表】-表单反馈导出_%s.xlsx' % today
wb = open_workbook(filename)
ttfont = ImageFont.truetype("/Library/Fonts/微软雅黑.ttf",40)

for s in wb.sheets():
	for row in range(2,s.nrows-3):
		values = []
		for col in range(s.ncols):
			values.append(s.cell(row,col).value)
		print values
		im = Image.open("template.jpg")  
		draw = ImageDraw.Draw(im)  
		draw.text((161,534),values[5], fill=(0,0,0),font=ttfont)  
		draw.text((161,735),values[6], fill=(0,0,0),font=ttfont)
		draw.text((161,935),values[7], fill=(0,0,0),font=ttfont)
		save_filename = u'%s需求.jpg' % values[2]
		im.save(save_filename)
		values = []
