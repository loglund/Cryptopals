# -*- coding: utf-8 -*-
"""
Detect AES in ECB mode. One ciphertext has been encrypted in ECB mode. Find it

Mikkel Højlund Larsen
"""
from Basics.AESinECB import getBlocks
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# will look for repetitions. AES in ECB is deterministic so prone to repetitions

def countRepetitions(ctext: bytes, block_size: int):
    chunks = [ctext[i : i + block_size] for i in range(0, len(ctext), block_size)]
    chunks = [tuple(chunk) for chunk in chunks]
    repetitionNumber = len(chunks) - len(set(chunks))
    result = {
            'ciphertext' : ctext,
            'repetitions' : repetitionNumber
    }
    return result

def DetectECB(ctext, block_size):
    repetitions = [countRepetitions(cipher, block_size) for cipher in ctext]
    #sort the lists of repetitions in descending order and choose the largest value
    mostRepetitions = sorted(repetitions, key=lambda x: x['repetitions'], reverse = True)[0]
    print("Ciphertext: {}".format(mostRepetitions['ciphertext']))
    print("Repeating Blocks: {}".format(mostRepetitions['repetitions']))
    if mostRepetitions['repetitions'] > 1:
        return True
    else:
        return False

"""
TEST
"""
#ciphertext = [bytes.fromhex(line.strip()) for line in open("DetectECB.txt")]
#print(DetectECB(ciphertext, 16))
    

