import os

def Zero(x,k):
  z = k-1
  if x > 9: z-=1
  if x > 99: z-=1
  if x > 999: z-=1
  if x > 9999: z-=1
  res = str(x)
  for i in range(z):
    res = "0"+res;
  return res

cf_files = []
c_files = []
r_files = []

for filename in os.listdir("."):
  if os.path.isfile(filename) and filename.endswith(".png") and filename.startswith("CF"):
    cf_files.append(filename)
  elif os.path.isfile(filename) and filename.endswith(".png") and filename.startswith("C"):
    c_files.append(filename)
  elif os.path.isfile(filename) and filename.endswith(".png") and filename.startswith("R"):
    r_files.append(filename)


cf_files.sort(key = (lambda x:int(x[2:x.find('.')])))
c_files.sort(key = (lambda x:int(x[1:x.find('.')])))
r_files.sort(key = (lambda x:int(x[1:x.find('.')])))

cf = open("cf40.txt","r").read().split("\r\n")
c = open("c40.txt","r").read().split("\r\n")
r = open("r40.txt","r").read().split("\r\n")

for i in range(len(cf_files)):
  os.system("cp "+cf_files[i]+" join/CF"+Zero(int(cf[i]),3)+".png")

for i in range(len(c_files)):
  os.system("cp "+c_files[i]+" join/C"+Zero(int(c[i]),3)+".png")

for i in range(len(r_files)):
  os.system("cp "+r_files[i]+" join/R"+Zero(int(r[i]),3)+".png")
