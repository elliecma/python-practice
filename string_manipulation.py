"""
This module transform data from a two column list to a list separated by a comma
followed by a space. The data can be found on page 92-93 of the following PDF:
http://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.0.0.pdf

The outcome should look like this:
    Other, Unknown, DRAM, EDRAM, VRAM, SRAM, RAM, ROM, FLASH, EEPROM, FEPROM, EPROM, CDRAM,
    3DRAM, SDRAM, SGRAM, RDRAM, DDR, DDR2, DDR2 FB-DIMM, Reserved, Reserved, Reserved, DDR3,
    FBD2, DDR4, LPDDR, LPDDR2, LPDDR3, LPDDR4

Author: elliecd@berkeley.edu
Created: 2015-08-25
Updated: 2015-08-26
"""

# open file
RAM_TYPES_FILE = open('RAMTypes.txt', 'r')

# create empty list
RAM_TYPES = list()

# split each line at the first space and keep the end, add to dataList
for line in RAM_TYPES_FILE:
	# http://www.tutorialspoint.com/python/string_split.htm
	# https://docs.python.org/2/library/string.html#string.split
    RAM = line.split(' ', 1)[-1]
	# https://docs.python.org/2/library/string.html#string.rstrip
	# https://docs.python.org/2/library/string.html#string.strip
    RAM_TYPES.append(RAM.rstrip())

# join items from dataList separated by comma + space
RAM_TYPES_FORMATTED = ', '.join(RAM_TYPES)

print RAM_TYPES_FORMATTED
