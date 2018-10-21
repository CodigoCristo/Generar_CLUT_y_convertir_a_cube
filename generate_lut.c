#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void save_targa(char *file_name, float *data, unsigned int x, unsigned int y)
{
	FILE *image;
	char *foot = "TRUEVISION-XFILES.";
	unsigned int i, j;

	if((image = fopen(file_name, "wb")) == NULL)
	{
		printf("Could not create file: %s\n", file_name);
		return;
	}
	fputc(0, image);
	fputc(0, image);
	fputc(2, image); /* uncompressed */

	for(i = 3; i < 12; i++)
		fputc(0, image); /* ignore some stuff */
	fputc(x % 256, image);  /* size */
	fputc(x / 256, image);
	fputc(y % 256, image);
	fputc(y / 256, image);

/* Clamping nod needed since clut is not HDRI */
/*	for(i = 0; i < 3 * x * y; i++) 
	{
		if(data[i] > 1)
			data[i] = 1;
		if(data[i] < 0)
			data[i] = 0;
	}
	*/

	fputc(24, image); /* 24 bit image */

	for(j = 0; j < y; j++)
	{
		for(i = 0; i < x; i++)
		{
			fputc((int)(data[((y - j - 1) * x + i) * 3 + 0] * 255.0), image);
			fputc((int)(data[((y - j - 1) * x + i) * 3 + 2] * 255.0), image);
			fputc((int)(data[((y - j - 1) * x + i) * 3 + 1] * 255.0), image);
		}
	}
	/* Footer not described in TARGA spec but for some reason needed by photoshop */
	for(i = 0; i < 9; i++)
		fputc(0, image); // ignore some stuff
	for(i = 0; foot[i] != 0; i++)
		fputc(foot[i], image); // ignore some stuff
	fputc(0, image);
	fclose(image);
}

int main(int argc, char **argv)
{
	char file_name [50];
	char nombre_archivo [500];
	char ext_tga [65] = ".tga";
	//color_Clut.tga
	unsigned int i, j, k, size, level = 0;
	float *data, *p;
	
	printf("\t/////////////////////////////////////////////\n");
	printf("\t\tGenerando Imagen Hald CLUT\n");
	printf("\thttp://www.quelsolaar.com/technology/clut.html\n");
	printf("\t/////////////////////////////////////////////\n\n");
	printf("Se recomienda usar el nivel 2 bits (tamaño 8 × 8 píxeles)\n");
	printf("Se recomienda usar el nivel 3 bits (tamaño 27 × 27 píxeles)\n");
	printf("Se recomienda usar el nivel 4 bits (tamaño 64 x 64 píxeles)\n");
	printf("Se recomienda usar el nivel 5 bits (tamaño 125 × 125 píxeles)\n");
	printf("Se recomienda usar el nivel 6 bits (tamaño 216 × 216 píxeles)\n");
	printf("Se recomienda usar el nivel 7 bits (tamaño 343 × 343 píxeles)\n");
	printf("Se recomienda usar el nivel 8 bits (tamaño 512 × 512 píxeles)\n\n"); 
	printf("\t****************************************************\n");
	printf("\t* Utilizando el nivel 8 = 3D LUT de tamaño standar *\n");
	printf("\t****************************************************\n");
	printf("\n"); 
	printf("El nivel 16 se recomienda para correcciones avanzadas\n"); 
	printf("Así como imágenes de 10, 12 y 16 bits.\n\n");
	printf("\tIngresa el nivel de calidad\n");
	printf("\t(Recomendado 2 a 16): ");
	scanf ("%i", &level);
	printf("\tNombre del archivo  : ");
	scanf ("%s", nombre_archivo); 	
	strcpy( file_name, nombre_archivo );
    strcat( file_name, ext_tga );
	
	
	if(argc > 1)
		
	
	if(argc > 2)
	{
		if(sscanf(argv[2], "%u", &level) != 1 || level > 1)
		{
			printf("Not valid level: %s (level must be %i or lower)\n", argv[2], level);
			exit(0);
		}
	}		
	size = level * level;
	data = p = malloc((sizeof *data) * size * size * size * 3);
	for(i = 0; i < size; i++) /**/
	{
		for(j = 0; j < size; j++)
		{
			for(k = 0; k < size; k++)
			{
				*p++ = (float)k / (float)(size - 1);
				*p++ = (float)j / (float)(size - 1);
				*p++ = (float)i / (float)(size - 1);
			}
		}
	}
	
	
	
	save_targa(file_name, data, level * level * level, level * level * level);
	printf("\n");
	printf("  Hald CLUT de %u bits fue creado, tamaño de %u por %u pixels.\n", level, size * level, size * level);
	printf("  Nombre de archivo: \t****  %s  ****\n\n", file_name);
	return 0;
}

