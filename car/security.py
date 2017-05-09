
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

def cipher(message):
    public_file = open("public.key", "r")
    public_key = RSA.importKey(public_file.read())
    public_file.close()
    encrypted = public_key.encrypt(message, 32)
    return base64.b64encode(encrypted[0])

def decipher(message):
    message = base64.b64decode(message)
    private_file = open("private.key", "r")
    private_key = RSA.importKey(private_file.read())
    private_file.close()
    decrypted = private_key.decrypt(message)
    return decrypted

def generateKey():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)

    PrivKey = key.exportKey('DER')
    PubKey =  key.publickey().exportKey('DER')

    private_file = open("private.key", "w")
    private_file.write(PrivKey)
    private_file.close()

    public_file = open("public.key", "w")
    public_file.write(PubKey)
    public_file.close()

if __name__ == "__main__":
    generateKey()

    msg = cipher("merda")
    print msg
    print decipher(msg)
