#/* ~~~
#python cube.py input.png output.cube
# .png .jpg .tar
# sRGB -> profile
# without understanding - sin comprensión (png)
#~~~

from __future__ import print_function, division

import math
import sys
from optparse import OptionParser

from PIL import Image


def main():

    opt_parser = OptionParser(usage='El uso es el siguiente: python %prog input.png output.cube')
    opts, args = opt_parser.parse_args()

    if len(args) != 2:
        opt_parser.print_usage()
        exit(1)

    in_ = Image.open(args[0])
    w, h = in_.size
    if w != h:
        print('La entrada HALD no es cuadrada.', file=sys.stderr)
        exit(2)
    steps = int(round(math.pow(w, 1/3)))
    if steps ** 3 != w:
        print('El tamaño de imagen no es válido: %d No se pudo generar cube.' % w, file=sys.stderr)
    
    print('\n')
    print('\t-------------------GRACIAS A:-----------------')
    print('\t----------------------------------------------')
    print('\t   https://github.com/mikeboers/LUT-Convert')
    print('\t----------------------------------------------')
    print('\n')
    print('\t----------------------------------------------')
    print('\tNivel de imagen de %d bits -> %d x %d Pixeles' % (steps, math.sqrt(steps**6), math.sqrt(steps**6)), file=sys.stderr)
    # Supongamos que vamos de 8 bits a 10.
    print('\t----------------------------------------------')

    out = open(args[1], 'w')
    out.write('LUT_3D_SIZE %d\n' % (steps ** 2))
    out.write('DOMAIN_MIN 0.0 0.0 0.0\n')
    out.write('DOMAIN_MAX 1.0 1.0 1.0\n')


    if False:
        steps1 = steps + 1
        steps3 = steps ** 2 * (steps + 1)
        steps5 = steps ** 4 * (steps + 1)
        data = list(in_.getdata())
        def lookup(ri, gi, bi):
            return data[
                ri * steps1 + gi * steps3 + bi * steps5
            ]
        for bi in xrange(steps):
            for gi in xrange(steps):
                for ri in xrange(steps):
                    r, g, b = lookup(ri, gi, bi)[:3]
                    out.write('%f %f %f\n' % (r / 255.0, g / 255.0, b / 255.0))
    else:
        for pixel in in_.getdata():
            r, g, b = pixel[:3]
            out.write('%f %f %f\n' % (r / 255.0, g / 255.0, b / 255.0))
    print('\n')
    print('\t\t/////////////////////////')
    print('\t\t     CUBE Realizado.')
    print('\t\t/////////////////////////')


if __name__ == '__main__':
    main()
