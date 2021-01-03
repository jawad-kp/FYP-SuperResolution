import argparse #to pass location
from threading import Thread
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import random


ap = argparse.ArgumentParser(description="Creat low-res copies of our data and add random noise to it") #Argument object
ap.add_argument("-l","--location", required = True, help="Path to data-set Folder")

args = vars(ap.parse_args())
# TODO: Run On Crappy() on GPU using FastAI's Parallel
def RSzer(im, ScaleVal):
    w,h = im.size
    return int(w*ScaleVal),int(h*ScaleVal)

class Crappifier():
	"""This class is responsible for resizing our image,adding compression artifacts and some randomly generated noise on top of that.
	We Pass the High-Res Path, Low-Res Folder and a scale factor that decides by how much we reduce image size"""
	def __init__(self,HresPath,LresPath,ScaleFactor):
		self.HresPath = HresPath
		self.LresPath = LresPath
		self.ScaleFactor = ScaleFactor
	def __call__(self,Fname,ShowPaths=False):
		Savepath = self.LresPath/Fname.relative_to(HiPath) #We do this because there's a way to parallely call the object on multiple files in FastAI which we can save for later
		ImgObj = Image.open(Fname)#open image
		TSze = RSzer(ImgObj,self.ScaleFactor)
		WasaImg = ImgObj.resize(TSze, resample=Image.BILINEAR).convert('RGB')
		q = random.randint(50,99)
		if (random.randint(1,2) == 2):
			ColorVals = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #Random RGB Values
			ImageDraw.Draw(WasaImg).text((random.randint(0,TSze[0]//2),random.randint(0,TSze[1]//2)), str(q), fill=ColorVals)
		WasaImg.save(Savepath,quality=q)
		if(ShowPaths):
			print(Savepath)


Pth = Path(args["location"]) 
HiPath = Pth/'Hi-Res'
LoPath = Pth/'Low-Res'


def MakeCrappy(LoPath,ScleF):
	Crappy = Crappifier(HiPath,LoPath,ScleF)
	for pt in HiPath.glob("*.*"):
		Crappy(pt, ShowPaths=True) #Comment this to stop seeing file names as it's done and uncomment the next line
		# Crappy(pt)

Pths = [LoPath/'OneHalf',LoPath/'OneFourth',LoPath/'OneEighth', LoPath/'OneSixteenth']
Scale = 0.5
MakeCrappyThrdLst = []
for P in Pths:
	CurThread = Thread(target=MakeCrappy,args=(P,Scale,))
	MakeCrappyThrdLst.append(CurThread)
	CurThread.start()
	Scale = Scale/2
[Thrd.join() for Thrd in MakeCrappyThrdLst]
print("Done!!")
		






