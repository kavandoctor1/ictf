def str_xor(data, key):
    for i in range(len(data)):
        data[i] ^= key[i % len(key)]
    return data

key  = bytearray(b'nice')
data = bytearray(open('xecret',  'rb').read())
encoded = str_xor(data, key)
open("ans.pdf", "wb").write(encoded)
# decoded = str_xor(data, key)
# open("data1.bin.xor.xor", "wb").write(decoded)