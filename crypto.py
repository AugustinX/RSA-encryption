# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:50:25 2017

@author: Administrator
"""

import Crypto
from Crypto.PublicKey import RSA



str1 = input('type in the line you wannna encrypt:\n')

#encryption
f = open('mypubkey.pem','r')
public_key1 = RSA.importKey(f.read())
f.close()

encrypted = public_key1.encrypt(str1.encode('utf-8'), 32)
print ('encrypted message:', encrypted[0])

f = open ('encryption', 'wb')
#write encrypted to file
f.write(encrypted[0])
f.close()

#decryption
f = open('myprikey.pem','r')
key1 = RSA.importKey(f.read())
f.close()


f = open ('encryption', 'rb')
message = f.read()
print (message)
print (type(message))


decrypted = key1.decrypt(message)

print ('decrypted', decrypted)

#write the decrpyted to a text file
f = open ('decryption.txt', 'w')
f.write(decrypted.decode('utf-8'))
f.close()
