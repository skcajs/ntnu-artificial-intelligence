import string
import random

def string2bin(string):
    return ''.join(format(ord(i), '08b') for i in string)


def swap(x):
    if x == '0':
        return '1'
    elif x == '1':
        return '0'
    else:
        return random.choice(string.ascii_lowercase + string.digits + string.punctuation + ' ')