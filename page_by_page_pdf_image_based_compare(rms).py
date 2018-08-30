import PythonMagick
from pdfrw import PdfReader, PdfWriter, PageMerge
from PIL import Image
import math
import operator
import os



h1 = Image.open("f1.PNG").histogram()
h2 = Image.open("f2.PNG").histogram()

rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

print (rms) 