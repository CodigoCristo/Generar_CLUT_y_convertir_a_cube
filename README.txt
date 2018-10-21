# Generar_CLUT_y_convertir_a_cube
# Archivos para generar un Clut y convertirlo a Cube. 

Si son usuarios ArchLinux hay que tener instalado. 
yaourt photivo
yaourt kdenlive 
sudo pacman -S gcc python 

http://photivo.org/download/linux 

paso para generar la imagen Clut<br>
gcc generate_lut.c -o nombre_del_programa<br>
<br>
paso para convertir la imagen a .cube o .3dl<br>
es necesario agregar la extesión .cube o .3dl <br>
python cube.py nombredeClut.png nombredelcube.cube<br>
python 3dl.py nombredeClut.png nombredel3dl.3dl <br>
<br>
se trabaja en formato de TGA de imagen para mejor calidad.<br> 
<br>
Tengo entendido la imagen que generamos en TGA se llama Clut<br>
Luego viene el proceso de exportarlo en png y convertirlo a Cube.<br> 
