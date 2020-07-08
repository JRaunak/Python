import math
public_key=[3127,5]
private_key=2413

def RSA_Encrypt(ascii):
    global public_key
    n=public_key[0]
    e=public_key[1]
    encrypted=pow(ascii,e,n)            # Similar to (ascii**e)%n
    return encrypted
 
def RSA_Decrypt(code):
    global public_key
    global private_key
    n=public_key[0]
    decrypted=pow(code,private_key,n)       # Similar to (code**private_key)%n
    return decrypted

action=input('Encrypt or Decrypt file: ')

if action=='Encrypt':
    filename=input('Enter File name containing message: ')
    messages=open(filename,'r')
    ciphered=open('Cipher.txt','w+')
    for message in messages:
        message=(message..strip())
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
    print('The encryted file is saved as "Cipher.txt" !!')

elif action=='Decrypt':
    filename=input('Enter File name containing message: ')
    secret_message=open(filename,'r')
    deciphered=open('Decipher.txt','w+')
    for message in secret_message:
        message=message..strip()
        decrypt=message.split()
        i=0
        decryptic=[]
        while i<len(decrypt):
            decryptic.append(chr(RSA_Decrypt(int(decrypt[i]))))
            i+=1
        j=0
        while j<len(decrypt):
            deciphered.write(decryptic[j])
            j+=1
        deciphered.write('\n')
    print('The decryted file is saved as "Decipher.txt" !!')

else:
    print('Invalid Option!!')  