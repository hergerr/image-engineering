#!/usr/bin/env python3
import numpy


width = 890 # 7*256/2
height = 80
max_value = 255

# PPM file header
ppm_ascii_header = f'P3 {width} {height} {max_value} ' 
ppm_binary_header = f'P6 {width} {height} {max_value} '

# image = numpy.array([1,1,1], dtype=numpy.uint8) 

red, green, blue = 1, 1, 1
lst = [red, green, blue]

while blue != max_value:
    blue += 2
    lst.extend([red, green, blue])

while green != max_value :
    green += 2
    lst.extend([red, green, blue])

while blue != 1 :
    blue -= 2
    lst.extend([red, green, blue])

while red != max_value :
    red += 2
    lst.extend([red, green, blue])

while green != 1:
    green -= 2
    lst.extend([red, green, blue])

while blue != max_value:
    blue += 2
    lst.extend([red, green, blue])

while green != max_value :
    green += 2
    lst.extend([red, green, blue])

# one row 
numpy_array = numpy.asarray(lst, dtype=numpy.uint8)
# repeat 'height' times
image = numpy.tile(numpy_array, (1, height))

# Save the PPM image as an ASCII file
with open('lab4-ascii.ppm', 'w') as fh:
    fh.write(ppm_ascii_header)
    image.tofile(fh, ' ')

    # does not work without new line at the end
    fh.write('\n')

# Save the PPM image as a binary file
with open('lab4-binary.ppm', 'wb') as fh:
    fh.write(bytearray(ppm_binary_header, 'ascii'))
    image.tofile(fh)
