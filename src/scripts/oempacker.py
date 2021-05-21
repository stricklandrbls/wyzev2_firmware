#!/usr/bin/env python3


import sys

class Firmware:
    def __init__(self, name, offset, size):
        self.name = name
        self.offset = offset
        self.size = size

firware_parts = [
    Firmware("uImage", 0x0, 0x40),
    Firmware("linux_kernel", 0x40, 0x200000),
    Firmware("sfs1", 0x200040, 0x350000),
    Firmware("sfs2", 0x550040, 0xa0000),
    Firmware("jffs2", 0x5f0040, 11075584-0x5f0040)
]

directory_output = "../firmware_images/"

if sys.argv[1] == '-h':
    print("Help page")
    exit()

if len(sys.argv) != 4:
    print(f"Command requires 3 arguements | {len(sys.argv)} provided\nType -h for help")
    exit()

if sys.argv[1] == "-u":
    if sys.argv[3][:2] == "-o":
        directory_output = sys.argv[4]
    
    f = open(sys.argv[2], "rb")

    for part in firware_parts:

        of = open(directory_output + part.name, "wb")

        data = f.read(part.size)

        of.write(data)
        of.close()
        print(f'Filename: {part.name} written')
        