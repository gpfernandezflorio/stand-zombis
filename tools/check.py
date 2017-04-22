import sys
import numpy as np

#f = open("js-grid-ar.json")
#f = open("js-grid-ba.json")
#f = open("js-grid-cp.json")
f = open("js-grid-cf.json")

s = f.read()

print "FILAS:", s.count('[')-1

h = s.split('[')

print "COLUMNAS:", h[2].count(',')
