# Generar_CLUT_y_convertir_a_cube
Archivos para generar un Clut y convertirlo a Cube. 

Si son usuarios ArchLinux hay que tener instalado. 
yaourt photivo
yaourt kdenlive
sudo pacman -S gcc python
http://photivo.org/download/linux

paso para generar la imagen Clut
gcc generate_lut.c -o nombre_del_programa

paso para convertir la imagen a .cube o .3dl
es necesario agregar la extesión .cube o .3dl 
python cube.py nombredeClut.png nombredelcube.cube
python 3dl.py nombredeClut.png nombredel3dl.3dl 

se trabaja en formato de TGA de imagen para mejor calidad. 

Tengo entendido la imagen que generamos en TGA se llama Clut
Luego viene el proceso de exportarlo en png y convertirlo a Cube. 
