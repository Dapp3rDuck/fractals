from PIL import Image 
from numpy import complex, array 
import colorsys
import math
import sys

print('Input Fractal in terms of z, reals, and c, complex:')

# Fractal basic info
FRACTAL = str(input('z = '))
FRACTAL.replace("^", "**")
ITERATIONS = int(input('Iterations: '))

# Domain input
x1, x2 = float(eval(str(input('Domain Start: ')))), float(eval(str(input('Domain End: '))))
y2, y1 = -1 * float(eval(str(input('Range Start: ')))), -1 * float(eval(str(input('Range End: '))))

# Grid
GRID = str(input('Display Grid (y/n): '))
GWIDTH, GHEIGHT, ROWS, COLUMNS = 1, 1, 1, 1 

if GRID == 'y':
    ROWS = int(input('Grid Rows: '))
    COLUMNS = int(input('Grid Columns: '))

WIDTH, HEIGHT = int(input('Width: ')), int(input('Height: '))
A, B = (x2 - x1) / WIDTH, (y2 - y1) / HEIGHT
GWIDTH, GHEIGHT = WIDTH/COLUMNS, HEIGHT/ROWS

#Progress Bar
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '▧' * filled_len + '□' * (bar_len - filled_len)

    sys.stdout.write('%s [%s] %s%s \r' % (status, bar, percents, '%'))
    sys.stdout.flush()

# Color converter
def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))

#Fractal Generator
def fractal(x, y):

    z, c = 0, complex(x1+x*A, y1+y*B)
    c = c

    if (x%(GWIDTH) > 0.75 or x%(GWIDTH) < -0.75) and (y%(GHEIGHT) > 0.75 or y%(GHEIGHT) < -0.75) and (y != (HEIGHT)-1) and (x != (WIDTH)-1) or (GRID != 'y'):

        for i in range(1, ITERATIONS):
            if abs(z) > 2: return rgb_conv(i)
            z = eval(FRACTAL)

        return (0, 0, 0)

    else: return (200, 200, 200)

img = Image.new('RGB', (WIDTH, HEIGHT))
pixels = img.load()

# Image Output
for x in range(img.size[0]):
    progress(x / WIDTH * 100.0, 100, 'Rendering...')
    for y in range(img.size[1]): pixels[x, y] = fractal(x, y)

img.save("sample.png", "")

# Text Output
y1, y2 = -1*y1, -1*y2
f = open('sample.txt', 'w')
f.write("Fractal: z = " + FRACTAL + '\n')
f.write("Domain: [{}, {}]\n".format(str(x1), str(x2)))
f.write("Range: [{}, {}]\n".format(str(y1), str(y2)))

if GRID == 'y':
    f.write("Grid: {}x{}\n".format(str(ROWS), str(COLUMNS)))
    f.write("Grid Cell width: {}\n".format(str((x2-x1)/COLUMS)))
    f.write("Grid Cell Height: {}\n".format(str((y2-y1)/ROWS)))

f.write("Resolution: {}x{}\n".format(str(WIDTH), str(HEIGHT)))
f.close()

progress(100, 100, 'Complete\n')