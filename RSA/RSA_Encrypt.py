import math
public_key=[3127,5]

def RSA_Encrypt(ascii):
    global public_key
    n=public_key[0]
    e=public_key[1]
    encrypted=pow(ascii,e,n)            # Similar to (ascii**e)%n
    return encrypted
 
filename=input('Enter File name containing message: ')
messages=open(filename,'r')
ciphered=open('CipherText.txt','w+')

for message in messages:
    message=(message.strip())
    i=0
    cryptic=[]
    while i<len(message):
        cryptic.append(RSA_Encrypt(ord(message[i])))
        i+=1
    j=0
    while j<len(message):
        ciphered.write(str(cryptic[j])+' ')
        j+=1
    ciphered.write('\n')