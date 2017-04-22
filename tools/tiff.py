from osgeo import gdal
from PIL import Image
import sys
import numpy as np

def vec(x):
  # ARGENTINA
  #z = list([0]*370) + list([0]*330) + list(x)[0:800]

  # BUENOS AIRES
  #z = list([0]*350) + list(x) + list([0]*150)

  # CONURBANO
  #z = list([0]*214) + list(x)

  # CAPITAL FEDERAL
  z = list([0]*388) + list(x)

  return z

def img(x):
  # ARGENTINA
  #z = np.concatenate((np.array([0]*370),np.array([0]*330),np.array(map(lambda y : inter(y), x)[0:800])))

  # BUENOS AIRES
  #z = np.concatenate((np.array([0]*350),np.array(map(lambda y : inter(y), x)),np.array([0]*150)))

  # CONURBANO
  #z = np.concatenate((np.array([0]*214),np.array(map(lambda y : inter(y), x))))

  # CAPITAL FEDERAL
  z = np.concatenate((np.array([0]*388),np.array(map(lambda y : inter(y), x))))

  return z

def inter(y):
  if y == 0:
    return 0.0
  else:
    return y+100

gdal.UseExceptions()

try:
  #src_ds = gdal.Open("arg.tiff")
  #src_ds = gdal.Open("ba.tiff")
  #src_ds = gdal.Open("cp.tiff")
  src_ds = gdal.Open("cf.tiff")
except RuntimeError, e:
  print 'failed'
  print e
  sys.exit(1)

print "[ RASTER BAND COUNT ]", src_ds.RasterCount

try:
  srcband = src_ds.GetRasterBand(1)
except RuntimeError, e:
  print 'failed'
  print e
  sys.exit(1)

print "[ NO DATA VALUE ]", srcband.GetNoDataValue()
print "[ MIN ]", srcband.GetMinimum()
print "[ MAX ]", srcband.GetMaximum()
print "[ SCALE ]", srcband.GetScale()
print "[ UNIT TYPE ]", srcband.GetUnitType()

ctable = srcband.GetColorTable()

if ctable is None:
  print 'No Color Table Found'
else:
  print "[ COLOR TABLE COUNT ]", ctable.GetCount()

myarray = np.array(src_ds.GetRasterBand(1).ReadAsArray())
m1 = map(lambda x : vec(x),list(myarray))
m2 = np.array(map(lambda x : img(x), myarray))

im = Image.open("blank.png")
pix = im.load()
for x in range(im.size[0]):
  for y in range(im.size[1]):
    v = int(m2[y,x])
    pix[x,y] = (v,v,v,255)

#im.save("js-ar.png")
#im.save("js-ba.png")
#im.save("js-cp.png")
im.save("js-cf.png")

m1.reverse()
#f = open("js-grid-ar.json",'w')
#f = open("js-grid-ba.json",'w')
#f = open("js-grid-cp.json",'w')
f = open("js-grid-cf.json",'w')
f.write(str(m1))
f.close()
