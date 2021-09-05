import cv2
import numpy as np
import glob
from pathlib import Path

def DoTheCrop(Img):
	Gray = cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
	_,thresh = cv2.threshold(Gray,1,255,cv2.THRESH_BINARY)
	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnt = contours[3]
	x,y,w,h = cv2.boundingRect(cnt)
	crop = Img[y:y+h,x:x+w]
	return crop

def ViewContour(Img,stem):
	Gray = cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
	_,thresh = cv2.threshold(Gray,1,255,cv2.THRESH_BINARY)
	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for i in range(len(contours)):
		Nu = Img.copy()
		cv2.drawContours(Nu, contours, i, (200,22,200), 3)
		title = stem+": "+str(i)
		cv2.imshow(title,Nu)
		cv2.waitKey(0)



i = 0
MySet = {'0825x3', '0812x3', '0829x3', '0808x3', '0822x3', '0881x3', '0845x3', '0870x3', '0803x3', '0816x3', '0859x3', '0849x3', '0802x3', '0819x3','0853x3', '0807x3', '0838x3', '0809x3', '0811x3', '0842x3', '0804x3', '0862x3', '0834x3', '0826x3', '0851x3', '0827x3', '0840x3', '0844x3', '0824x3', '0810x3', '0801x3', '0843x3', '0823x3', '0848x3', '0830x3', '0837x3', '0831x3', '0821x3', '0836x3', '0833x3', '0806x3', '0854x3', '0815x3', '0820x3', '0828x3', '0850x3', '0814x3', '0818x3', '0892x3', '0832x3', '0841x3', '0817x3','0855x3'}

SaveFolder = Path('MyOuts/')
for fileName in glob.glob("C:/Users/Jawad/Documents/FYP-SuperResolution/Results/X3ToX2Png/content/OurPngs/*.png"):
	OgPath = Path(fileName)
	img = cv2.imread(str(OgPath))
	if(OgPath.stem not in MySet):
		ViewContour(img,OgPath.stem)
	# # # else:
	# 	# img = cv2.imread(str(OgPath))
	# 	SavePath = SaveFolder/(OgPath.stem+".png")
	# 	# print(SavePath)
	# 	# cv2.imshow("Is A work?",img)
	# 	# cv2.waitKey(0)
	# 	try:
	# 		CropImg = DoTheCrop(img)
	# 		cv2.imwrite(str(SavePath),CropImg)			
	# 	except Exception as e:
	# 		print(OgPath.stem+" gave an exception")
		# cv2.imshow("Is A work?",CropImg)
		# cv2.waitKey(0)