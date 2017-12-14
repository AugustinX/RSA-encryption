# RSA-encryption
this project is simply a test of RSA assymmetric encryption.
the software was built on Python 3.6.

two files:
  crypto.py: is to implement the key to encrypt and decrypt the text. Chinese/English/French are tested for the input, utf-8 works well.
  keygen.py: randomly generates a pair of key for later use.

it can be used for secured data transmission which is especially important in the countries where surveillance conducted by goverment against ordinary people is very common.

How to use:
publish the pubkey file (PEM) to your peers, they use a modified code of the "crypto.py" (with public key) to encrypt. then send the encrypted file to you. Similarly you use it (with private key) to decrypt. Notice: DON'T PUBLISH YOUR PRIVATE KEY!
