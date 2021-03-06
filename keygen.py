# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 12:28:15 2017

@author: Administrator
"""

from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate public and private keys
f = open('myprikey.pem','wb')
f.write(key.exportKey('PEM'))
f.close()

public_key = key.publickey() # pub key export for exchange
f = open('mypubkey.pem','wb')
f.write(public_key.exportKey('PEM'))
f.close()

print(public_key)