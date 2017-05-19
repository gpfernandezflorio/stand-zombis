import os

frame_rate = 24

files = []

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

for filename in os.listdir("."):
  if filename != "gen.py":
    files.append(filename)


K = len(files)

k=1
if K > 9: k+=1
if K > 99: k+=1
if K > 999: k+=1
if K > 9999: k+=1

files = sorted(files, key = lambda x : int(x[1:x.find(".")]))

for i in range(K):
  os.rename(files[i],"A"+Zero(i,k)+".png")

os.system("ffmpeg -framerate "+str(frame_rate)+" -i A%0"+str(k)+"d.png output.mp4")
