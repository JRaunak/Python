import math
public_key=[3127,5]
private_key=2413

def RSA_Decrypt(code):
    global public_key
    global private_key
    n=public_key[0]
    decrypted=pow(code,private_key,n)       # Similar to (code**private_key)%n
    return decrypted
    
filename=input('Enter File name containing message: ')
secret_message=open(filename,'r')
deciphered=open('DeCipherText.txt','w+')

for message in secret_message:
    message=message.strip()
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