import cv2 as cv
import numpy as np
from pathlib import Path


def Split_Video(PathToVid,StartTime,NumFrames,SaveLoc):
	'''This function breaks up a video and captures only the frames you need'''
	cap = cv.VideoCapture(str(PathToVid))
	frameRate = cap.get(cv.CAP_PROP_FPS)
	StartTimeInSec = StartTime*60
	StartFrame = StartTimeInSec*frameRate
	FrameCount = 0
	Duration = 10
	cap.set(cv.CAP_PROP_POS_FRAMES,StartFrame)
	while cap.isOpened:
		FrameCount += 1
		ret, frame = cap.read()
		name = SaveLoc/(str(FrameCount)+".png")
		cv.imwrite(str(name),frame)
		if(FrameCount == NumFrames):
			break
	cap.release()
	print("All Done!!")
# Making it a square

# ScaleDown -> Resize -> Save
def DownScale(img,ScalePerc):
	width = int(img.shape[1] * ScalePerc / 100)
	height = int(img.shape[0] * ScalePerc / 100)
	dim = (width, height)
	return cv.resize(img, dim, interpolation = cv.INTER_AREA)
def GetSquare(img):
	StartIndHt = int((img.shape[0]-680)/2)
	EndIndHt = int((StartIndHt+680))
	StartIndWd = int((img.shape[1]-680)/2)
	EndIndWd = int((StartIndWd+680))
	return img[StartIndHt:EndIndHt,StartIndWd:EndIndWd]

SaveFolder = Path("frames\\SquareFrames")
FrameLoc = Path("frames\\FullFrames")

for FilePath in FrameLoc.glob("*.png"):
	img = GetSquare(DownScale(cv.imread(str(FilePath)),65))
	SavePath = SaveFolder/FilePath.name
	cv.imwrite(str(SavePath),img)

print("All Done!!")






