import cv2 as cv
import numpy as np
from pathlib import Path

fourcc = cv.VideoWriter_fourcc(*'DIVX')
Out = cv.VideoWriter('UpscaledFile-DIVX.avi', fourcc, 24.0, (680,680),True)
FrameLoc = Path("frames/VideoFrames-Upscaled")
FramNum = 1
LastFrame = 240
for FramNum in range(1,LastFrame+1):
	FilePath = FrameLoc/(str(FramNum)+".png")
	Out.write(cv.imread(str(FilePath)))
Out.release()
print("All Done!!")