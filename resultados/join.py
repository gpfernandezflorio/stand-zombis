import os

hours_per_pic = 10
frame_rate = 18

cf_files = []
c_files = []
r_files = []

def next_pic(files,frame,x,y):
  result = files[0]
  for i in files:
    seq = int(i[x:y])
    if seq >= frame:
      return result
    result = i
  return result

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
  if os.path.isfile(filename) and filename.endswith(".png") and filename.startswith("Z-CF"):
    cf_files.append(filename)
  elif os.path.isfile(filename) and filename.endswith(".png") and filename.startswith("Z-C"):
    c_files.append(filename)
  elif os.path.isfile(filename) and filename.endswith(".png") and filename.startswith("Z-R"):
    r_files.append(filename)

cf_files.sort()
c_files.sort()
r_files.sort()

M = int(cf_files[len(cf_files)-1][5:8])
m = int(c_files[len(c_files)-1][4:7])
if m > M:
  M = m
m = int(r_files[len(r_files)-1][4:7])
if m > M:
  M = m
print M

K = (M+1)/hours_per_pic

cf_pics = []
for i in range(K):
  cf_pics.append(next_pic(cf_files,i*hours_per_pic,5,8))

c_pics = []
for i in range(K):
  c_pics.append(next_pic(c_files,i*hours_per_pic,4,7))

r_pics = []
for i in range(K):
  r_pics.append(next_pic(r_files,i*hours_per_pic,4,7))

k=1
if K > 9: k+=1
if K > 99: k+=1
if K > 999: k+=1
if K > 9999: k+=1

for i in range(K):
  os.system("convert "+cf_pics[i]+" "+c_pics[i]+" "+r_pics[i]+" +append A"+Zero(i,k)+".png")
os.system("ffmpeg -framerate "+str(frame_rate)+" -i A%0"+str(k)+"d.png output.mp4")
