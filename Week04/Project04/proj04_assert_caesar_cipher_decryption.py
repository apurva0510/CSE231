from proj04 import caesar_cipher_decryption

print("caesar_cipher_decryption('d',3,'abcdefgh'):",caesar_cipher_decryption('d',3,'abcdefgh'))
print("caesar_cipher_decryption('8',3,'2cdef78h'):", caesar_cipher_decryption('8',3,'2cdef78h')) 

assert caesar_cipher_decryption('d',3,'abcdefgh') == 'a'
assert caesar_cipher_decryption('8',3,'2cdef78h') == 'e'
