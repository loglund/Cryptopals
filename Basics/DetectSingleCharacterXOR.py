# -*- coding: utf-8 -*-
"""
Detect single-byte XOR cipher using a list of 60 character strings with a single one encrypted.

Mikkel Højlund Larsen
"""
import SingleByteXorCipher

f = open("listOfPossibleCiphers.txt")
f_list = f.readlines()

for i in range(len(f_list)):
    f_list[i] = bytes.fromhex(f_list[i])


def DetectXOR(stringlist: list):
    minFQlist = 0
    fulllist = []
    for i in range(len(stringlist)):
        fulllist.append(SBXORDecipher(stringlist[i]))
        if minFQlist == 0 or fulllist[i][2]< minFQlist:
            minFQlist = fulllist[i][2]
            j = i
    print(fulllist[j])
    return fulllist[j]


DetectXOR(f_list)