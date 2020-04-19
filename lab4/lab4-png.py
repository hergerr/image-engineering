#!/usr/bin/env python3
import numpy
import struct
import zlib

# Image data
image = numpy.array([[[255,   0,   0], [0, 255,  0]],
                     [[0,   0, 255], [55,  55,  0]]],
                    dtype=numpy.uint8)

# Construct signature
png_file_signature = b"\x89" + \
    "PNG\r\n\x1A\n".encode('ascii')  # TODO: implement
h, w, _ = image.shape

# Construct header
# ! big endian, I - 4b unsigned int, B 1B unsigned char 
header_id = b'IHDR'
header_content = struct.pack('!IIBBBBB', w, h, 8, 2, 0, 0, 0)
header_size = struct.pack('!I', len(header_content))    # it means unsigned int
header_crc = struct.pack('!I', zlib.crc32(header_id + header_content))
png_file_header = header_size + header_id + header_content + header_crc

# Construct data
data_id = b'IDAT'
idat = numpy.empty((h, w*3 + 1), dtype=numpy.uint8)
idat[:, 1:] = image.reshape(h, w*3)
idat[:, 0] = 0

data_content = zlib.compress(idat, 9)
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
