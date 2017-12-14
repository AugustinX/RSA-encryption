# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:50:25 2017

@author: Administrator
"""

import Crypto
from Crypto.PublicKey import RSA



str1 = input('type in the line you wannna encrypt:\n')

f = open('mypubkey.pem','r')
public_key1 = RSA.importKey(f.read())
f.close()

encrypted = public_key1.encrypt(str1.encode('utf-8'), 32)
#message to encrypt is in the above line 'encrypt this message'

print ('encrypted message:', encrypted[0]) #ciphertext


f = open ('encryption', 'wb')
f.write(encrypted[0]) #write ciphertext to file
f.close()

#decrypted code below
f = open('myprikey.pem','r')
key1 = RSA.importKey(f.read())
f.close()


f = open ('encryption', 'rb')
message = f.read()
print (message)
print (type(message))


decrypted = key1.decrypt(message)

print ('decrypted', decrypted)

f = open ('decryption.txt', 'w')
#f.write(str(message))
f.write(decrypted.decode('utf-8'))
f.close()
