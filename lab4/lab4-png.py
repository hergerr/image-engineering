#!/usr/bin/env python3
import numpy
import struct
import zlib

height = 80
max_value = 255

red, green, blue = 1, 1, 1
row = numpy.array([red, green, blue], dtype=numpy.uint8)

while blue != max_value:
    blue += 2
    row = numpy.vstack([row, [red, green, blue]])

while green != max_value:
    green += 2
    row = numpy.vstack([row, [red, green, blue]])

while blue != 1:
    blue -= 2
    row = numpy.vstack([row, [red, green, blue]])

while red != max_value:
    red += 2
    row = numpy.vstack([row, [red, green, blue]])

while green != 1:
    green -= 2
    row = numpy.vstack([row, [red, green, blue]])

while blue != max_value:
    blue += 2
    row = numpy.vstack([row, [red, green, blue]])

while green != max_value:
    green += 2
    row = numpy.vstack([row, [red, green, blue]])


image = numpy.repeat(row[numpy.newaxis, ...], height, axis=0)

# Construct signature
png_file_signature = b"\x89" + "PNG\r\n\x1A\n".encode('ascii')
h, w, _ = image.shape

# Construct header
# ! big endian, I - 4b unsigned int, B 1B unsigned char
header_id = b'IHDR'
header_content = struct.pack('!IIBBBBB', w, h, 8, 2, 0, 0, 0)
header_size = struct.pack('!I', len(header_content))    # it means unsigned int
header_crc = struct.pack('!I', zlib.crc32(header_id + header_content))
png_file_header = header_size + header_id + header_content + header_crc

# Construct data
# no idea why w*3 needs + 1 in reshape
data_id = b'IDAT'
zero_byte_data = numpy.empty((h, w*3 + 1), dtype=numpy.uint8)

# reshaping from 3D to 2D wih 2D with 0 byte
zero_byte_data[:, 1:] = image.reshape(h, w*3)
zero_byte_data[:, 0] = 0

data_content = zlib.compress(zero_byte_data, 9)
data_size = struct.pack('!I', len(data_content))
data_crc = struct.pack('!I', zlib.crc32(data_id + data_content))
png_file_data = data_size + data_id + data_content + data_crc

# Consruct end
end_id = b'IEND'
end_content = b''
end_size = struct.pack('!I', len(end_content))
end_crc = struct.pack('!I', zlib.crc32(end_id + end_content))
png_file_end = end_size + end_id + end_content + end_crc

# Save the PNG image as a binary file
with open('lab4.png', 'wb') as fh:
    fh.write(png_file_signature)
    fh.write(png_file_header)
    fh.write(png_file_data)
    fh.write(png_file_end)
