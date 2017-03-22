import os

for filename in os.listdir("."):
  if os.path.isfile(filename) and filename.endswith(".png"):
    newname = "Z-"+filename
    print newname
    os.system("convert "+filename+" -crop 415x768+635+0 "+newname)
