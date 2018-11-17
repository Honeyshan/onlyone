import os
import os.path
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

######################获取同一个文件夹下的所有PDF文件名#######################
def getFileName(filepath):
	file_list = []
	for root, dirs, files in os.walk(filepath):
		for filespath in files:
			# 如果该文件夹下有png文件，则将其转换为pdf
			if filespath.endswith('.png'):
				newpath = ''.join(filespath[:-4]) + '.pdf'
				conpdf(os.path.join(root, filespath), os.path.join(root + newpath))
				file_list.append(os.path.join(root, newpath))
			else:
				file_list.append(os.path.join(root, filespath))
	# 排序
	file_list.sort()
	return file_list

#######################合并同一个文件夹下所有PDF文件#######################
def MergePDF(filepath, outfile):
	output = PdfFileWriter()
	outputPages = 0
	pdf_fileName = getFileName(filepath)
	for each in pdf_fileName:
		print(each)
		print('-=-=' * 30)
		# 读取源pdf文件
		# with open(each,'rb') as f:
		input = PdfFileReader(open(each, 'rb'))
		# 获得源pdf文件中页面总数
		pageCount = input.getNumPages()
		outputPages += pageCount
		print(pageCount)
		# 分别将page添加到输出output中
		for iPage in range(0, pageCount):
			output.addPage(input.getPage(iPage))
	print("All Pages Number:" + str(outputPages))
	# 最后写pdf文件
	# with open(filepath + outfile, "wb") as outputStream:
	outputStream = open(filepath + outfile, "wb")
	output.write(outputStream)
	outputStream.close()
	print(outputPages)
	print("finished")

#######################将某一个文件夹下的png转换为pdf#######################
def conpdf(filePath, newPath):
	(w, h) = landscape(A4)
	c = canvas.Canvas(newPath, pagesize=landscape(A4))
	c.drawImage(filePath, 0, 0, w, h)
	c.save()

if __name__ == '__main__':
	time1 = time.time()
	dir = input('文件夹名字')
	file = r'%s\\' % dir
	number = dir[-12:-8] + 'draftreturn201810'
	out = u"%s.pdf" % number
	MergePDF(file, out)
	time2 = time.time()
