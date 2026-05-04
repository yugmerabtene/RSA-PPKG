import os
import ftplib
import hashlib
from Crypto.PublicKey import RSA
from Crypto import Random
from dotenv import load_dotenv

load_dotenv()

def generate_rsa_keys():
    random_generator = Random.new().read
    print('Génération des clés...')
    key = RSA.generate(2048, random_generator)
    
    pub_key = key.publickey().exportKey("PEM")
    pri_key = key.exportKey("PEM")
    
    with open('pub_key.pem', 'wb') as f:
        f.write(pub_key)
    
    with open('pri_key.pem', 'wb') as f:
        f.write(pri_key)
    
    print('Clés exportées dans pub_key.pem et pri_key.pem')
    return pub_key, pri_key

def hash_file(filename):
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    
    with open(filename, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    
    return file_hash.hexdigest()

def send_to_ftp():
    FTP_HOST = os.getenv('FTP_HOST', '')
    FTP_USER = os.getenv('FTP_USER', '')
    FTP_PASS = os.getenv('FTP_PASS', '')
    
    if not all([FTP_HOST, FTP_USER, FTP_PASS]):
        print('Configuration FTP manquante dans .env')
        return False
    
    try:
        print('Connexion au serveur FTP...')
        ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        ftp.encoding = "utf-8"
        
        for filename in ['pri_key.pem', 'pub_key.pem']:
            with open(filename, "rb") as file:
                ftp.storbinary(f"STOR {filename}", file)
            print(f'{filename} envoyé')
        
        ftp.dir()
        ftp.quit()
        return True
    except Exception as e:
        print(f'Erreur FTP: {e}')
        return False

def cleanup():
    for filename in ['pri_key.pem', 'pub_key.pem']:
        if os.path.exists(filename):
            os.remove(filename)
    print('Fichiers locaux supprimés')

if __name__ == '__main__':
    pub_key, pri_key = generate_rsa_keys()
    
    print('Empreinte clé publique:', hash_file('pub_key.pem'))
    print('Empreinte clé privée:', hash_file('pri_key.pem'))
    
    if send_to_ftp():
        cleanup()
    
    print('Terminé')
