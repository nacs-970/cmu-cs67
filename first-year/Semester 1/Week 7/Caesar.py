import string
def caesar_cipher(text,shift,decode=False):
    alpha = string.ascii_lowercase
    if decode: shift = -shift # move back ward
    shifted_table = alpha[shift:] + alpha[0:shift]
    print(shifted_table)
    text = text.lower()
    ori_pos = list(map(lambda x: alpha.find(x),text))
    #return ori_pos # index of string from table 7, 0, 15, 15, 24 kdssd
    encoded = list(map(lambda x: shifted_table[x],ori_pos))
    return ''.join(encoded)
print(caesar_cipher("happy", 3)) # happy kdssb
print(caesar_cipher("kdssb", 3,True)) # happy kdssb
