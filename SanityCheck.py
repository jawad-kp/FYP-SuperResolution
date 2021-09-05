# import cv2
# import numpy as np
import glob
from pathlib import Path

MySet = set()
for fileName in glob.glob("MyOuts/*.png"):
	OgPath = Path(fileName)
	MySet.add(OgPath.stem)
print(MySet)
