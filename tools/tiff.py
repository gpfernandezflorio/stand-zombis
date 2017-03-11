from osgeo import gdal
import sys
import numpy as np
import matplotlib.pyplot as plt

def vec(x):
  # ARGENTINA
  z = list([0]*370) + list([0]*330) + list(x)[0:800]

  # BUENOS AIRES
  #z = list([0]*350) + list(x) + list([0]*150)

  # CAPITAL FEDERAL
  #z = list([0]*214) + list(x)

  #z = list(x)
  return z

def img(x):
  # ARGENTINA
  z = list([0]*370) + list([0]*330) + list(map(lambda y : inter(y), x)[0:800])

  # BUENOS AIRES
  #z = list([0]*350) + list(map(lambda y : inter(y), x)) + list([0]*150)

  # CAPITAL FEDERAL
  #z = list([0]*214) + list(map(lambda y : inter(y), x))

  #z = list(map(lambda y : inter(y), x))
  return z

def inter(y):
  if y == 0:
    return 0.0
  else:
    return y+100

gdal.UseExceptions()

try:
  src_ds = gdal.Open("arg.tiff")
  #src_ds = gdal.Open("ba.tiff")
  #src_ds = gdal.Open("cp.tiff")
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
m2 = map(lambda x : img(x),list(myarray))

plt.imshow(m2)
plt.xticks([])
plt.yticks([])
plt.savefig("js-ar.png",dpi=500)
#plt.savefig("js-ba.png",dpi=500)
#plt.savefig("js-cp.png",dpi=500)

m1.reverse()
f = open("js-grid-ar.json",'w')
#f = open("js-grid-ba.json",'w')
#f = open("js-grid-cp.json",'w')
f.write(str(m1))
f.close()
