import argparse #to pass location
import cv2 as cv
import glob #to open folder

# TODO: Add noise and compression artifacts to images apart from lower resolution

ap = argparse.ArgumentParser(description="Creat low-res copies of our data and add random noise to it") #Argument object
ap.add_argument("-l","--location", required = True, help="Path to data-set Folder")

args = vars(ap.parse_args())

def DownScaler(OgImg, ScaleFactor,FName, Folder):
	width = int(OgImg.shape[1] * ScaleFactor)
	height = int(OgImg.shape[0] * ScaleFactor)
	dim = (width,height) 
	im = cv.resize(img, dim, interpolation = cv.INTER_AREA)
	cv.imwrite(Folder+FName,im)


# count = 0
# TODO: Make Multi-Threaded (?)
St = len(args["location"])+7
HalfLoc = args["location"]+"\\Low-Res\\OneHalf"
FourthLoc = args["location"]+"\\Low-Res\\OneFourth"
EighthLoc = args["location"]+"\\Low-Res\\OneEighth"
SixteenthLoc = args["location"]+"\\Low-Res\\OneSixteenth"
for imagePath in glob.glob(args["location"]+"\\Hi-Res\\*.*"):
	img = cv.imread(imagePath,cv.IMREAD_UNCHANGED)
	Fnm = imagePath[St:]
	DownScaler(img,0.5,Fnm,HalfLoc)
	DownScaler(img,0.25,Fnm,FourthLoc)
	DownScaler(img,0.125,Fnm,EighthLoc)
	DownScaler(img,0.0625,Fnm,SixteenthLoc)	
	# if count >=3:
	# 	break
	# count += 1






