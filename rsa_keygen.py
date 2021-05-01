import os
import ftplib # module ftp
import hashlib # module de hash de fichier
from Crypto.PublicKey import RSA #import crypto module enabling RSA
from Crypto import Random #  import random-generator from Crypto
random_generator = Random.new().read # generer un nombre et le mettre
print ('generating keys please wait')
key = RSA.generate(2048, random_generator) # generer une cle + un nombre aléatoire
pub_key = key.publickey().exportKey("PEM") # mettre en memoire la cle generee
pri_key = key.exportKey("PEM") # mettre en memoire la cle generée
print (pub_key)
print (pri_key)
print ('exporting keys to files')
with open('pub_key.pem', 'wb') as f: # mettre la cle pub dans un fichier
    f.write(pub_key)
    f.close()
with open('pri_key.pem', 'wb') as f: # mettre la cle privée dans un fichier 
	f.write(pri_key)
	f.close ()
print ('Keys Exported Into a file Job done')

#HASHING KEYS POUR GARDER UN FINGERPRINT
print ('public key hash')
file = "pub_key.pem" # Location of the file (can be set a different way)
BLOCK_SIZE = 65536 # The size of each read from the file
file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        file_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file

print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash

#HASHING KEYS POUR GARDER UN FINGERPRINT
print ('private key HASH')
file = "pri_key.pem" # Location of the file (can be set a different way)
BLOCK_SIZE = 65536 # The size of each read from the file
file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        file_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file

print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash

print ('CONNECTING TO FTP SERVER')
# sending keys to an ftp server
FTP_HOST = ""
FTP_USER = ""
FTP_PASS = ""
print ('connected')
# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

print ('SENDING FILES TO THE SERVER')
# local file name you want to upload
filename = "pri_key.pem"
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary(f"STOR {filename}", file)

filename = "pub_key.pem"
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary(f"STOR {filename}", file)
    print ('Printing FTP FOLDER')
    ftp.dir()
print ('deleting local keys files')
os.remove("pri_key.pem")
os.remove("pub_key.pem")
print ('All done :-)')
