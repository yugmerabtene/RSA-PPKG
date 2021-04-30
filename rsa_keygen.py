from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
pub_key = key.publickey().exportKey("PEM")
pri_key = key.exportKey("PEM")
print (pub_key)
print (pri_key)
print ('exporting keys')
with open('pub_key.pem', 'wb') as f:
    f.write(pub_key)
    f.close()
with open('pri_key.pem', 'wb') as f:
	f.write(pri_key)
	f.close ()
