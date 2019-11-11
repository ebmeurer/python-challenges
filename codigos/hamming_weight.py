'''
Write a function that takes an unsigned integer and returns the number of 1 bits it has (also known as the Hamming weight).

For example:

The 32-bit integer 11 has binary representation 00000000000000000000000000001011, so the function should return 3.
'''

def hamming_weight(num):
    binario = list(str(bin(num)).split('0b')[1])
    return binario.count('1')
    
print(hamming_weight(11))
