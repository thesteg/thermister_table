#!/usr/bin/python

import math
import sys

#bValue = float(sys.argv[1])
#nomOhm = float(sys.argv[2])
#nomTemp = float(sys.argv[3])
#seriesR = float(sys.argv[4])
#adcRes = int(sys.argv[5])

bValue = 3750
nomOhm = 10000
nomTemp = 250
seriesR = 4700
adcRes = 10

adcMax = 2**adcRes
adcVal = 0

vals = [0] * adcMax

while adcVal < adcMax:
    try:
        vals[adcVal] = 10 / ((math.log((seriesR / (((adcMax - 1) / adcVal) -1)) / nomOhm) / bValue) + (10 / (nomTemp + 2731.5))) -2731
        adcVal += 1
    except:
        adcVal += 1

print("int16_t tVals[{0}] = {{".format(adcMax))

adcVal = 0

while adcVal < adcMax:
    print("    {0},{1},{2},{3},{4},{5},{6},{7},"
        .format(
            round(vals[adcVal]),
            round(vals[adcVal + 1]),
            round(vals[adcVal + 2]),
            round(vals[adcVal + 3]),
            round(vals[adcVal + 4]),
            round(vals[adcVal + 5]),
            round(vals[adcVal + 6]),
            round(vals[adcVal + 7]),
            ))

    adcVal += 8

print("};\n")