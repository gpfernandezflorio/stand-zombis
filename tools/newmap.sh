# Paso 1: Recortar el mapa. Ignorar si se va a usar el mapa completo

# Buenos Aires:
#rm -f ba.tif*
#gdalwarp -te -65 -41 -55 -32 ../../../ARGPOP/ARG_ppp_v2b_2010.tif ba.tif

# Conurbano
#rm -f cp.tif*
#gdalwarp -te -59 -35 -58 -34.3 ../../../ARGPOP/ARG_ppp_v2b_2010.tif cp.tif

# Capital Federal
rm -f cf.tif*
gdalwarp -te -58.56 -34.7 -58.35 -34.53 ../../../ARGPOP/ARG_ppp_v2b_2010.tif cf.tif



# Paso 2: Redimensionar la imagen

# Argentina:
#gdalwarp -dstnodata 0 -ts 0 900 -r near ../../ARGPOP/ARG_ppp_v2b_2010.tif arg.tiff

# Buenos Aires:
#gdalwarp -dstnodata 0 -ts 0 900 -r near ba.tif ba.tiff

# Conurbano
#gdalwarp -dstnodata 0 -ts 0 900 -r near cp.tif cp.tiff

# Capital Federal
gdalwarp -dstnodata 0 -ts 0 900 -r cubic cf.tif cf.tiff



# Paso 3: Generar matriz (.json) e imagen de fondo (.png)
python tiff.py



# Paso 4: Chequear cantidad de filas y columnas
python check.py
# La cantidad de filas debería ser 900
# Si la cantidad de columnas es menor a 1500, rellenar en las funciones 'vec' y 'img' de tiff.py
