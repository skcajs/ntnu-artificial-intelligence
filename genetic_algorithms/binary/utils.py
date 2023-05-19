import string
import random
import struct
from codecs import decode


def string_to_bin(string):
    return ''.join(format(ord(i), '08b') for i in string)

def float_to_bin(num):
    return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def swap(x):
    if x == '0':
        return '1'
    elif x == '1':
        return '0'
    else:
        return random.choice(string.ascii_lowercase + string.digits + string.punctuation + ' ')