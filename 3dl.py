#/* ~~~
# python cube.py input.png output.3dl
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
    print('\n\t----------------------------------------------')
    print("\tAdvertencia: No devuelve resultados precisos.", file=sys.stderr)
    print('\t----------------------------------------------')
    
    opt_parser = OptionParser(usage='El uso es el siguiente: %prog [+opciones] input.png output.3dl')
    opts, args = opt_parser.parse_args()

    if len(args) != 2:
        opt_parser.print_usage()
        exit(1)

    in_ = Image.open(args[0])
    w, h = in_.size
    if w != h:
        print('La entrada de imagen no es cuadrada.', file=sys.stderr)
        exit(2)
    steps = int(round(math.pow(w, 1/3)))
    if steps ** 3 != w:
        print('El tamaño de imagen no es válido: %d No se pudo generar 3dl.' % w, file=sys.stderr)
        
    print('\n')
    print('\t----------------------------------------------')
    print('\t\t  Nivel de imagen de %d bits' % steps, file=sys.stderr)
    # Supongamos que vamos de 8 bits a 10.
    print('\t----------------------------------------------')

    out = open(args[1], 'w')
    header = [1023 * i // (steps - 1) for i in range(steps)]
    out.write(' '.join(str(x) for x in header))
    out.write('\n')

    steps1 = steps + 1
    steps3 = steps ** 2 * (steps + 1)
    steps5 = steps ** 4 * (steps + 1)
    data = list(in_.getdata())
    def lookup(ri, gi, bi):
        return data[
            ri * steps1 + gi * steps3 + bi * steps5
        ]
    for ri in range(steps):
        for gi in range(steps):
            for bi in range(steps):
                r, g, b = lookup(ri, gi, bi)
                out.write('%d %d %d\n' % (r * 4, g * 4, b * 4))

    print('\n')
    print('\t\t  /////////////////////////')
    print('\t\t       3dl Realizado.')
    print('\t\t  /////////////////////////')

if __name__ == '__main__':
    main()