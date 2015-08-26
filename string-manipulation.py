# transform data from two column list to list separated by comma followed by a space
# data found on pg 92-93 : http://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.0.0.pdf
#
# outcome should look like this:
# Other, Unknown, DRAM, EDRAM, VRAM, SRAM, RAM, ROM, FLASH, EEPROM, FEPROM, EPROM, CDRAM, 3DRAM, SDRAM, SGRAM, RDRAM, DDR, DDR2, DDR2 FB-DIMM, Reserved, Reserved, Reserved, DDR3, FBD2, DDR4, LPDDR, LPDDR2, LPDDR3, LPDDR4
#
# 8/25/14 elliecd@berkeley.edu

# open file
data = open('RAMTypes.txt','r')

# create empty list
dataList = list()

# split each line at the first space and keep the end, add to dataList
for line in data :
	lineItem = line.split(' ', 1)[-1]
	dataList.append(lineItem.rstrip())

# join items from dataList separated by comma + space
output = ', '.join(dataList)

print output
