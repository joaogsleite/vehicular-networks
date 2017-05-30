
from Crypto.PublicKey.RSA import importKey, generate
from Crypto import Random
from base64 import b64encode, b64decode

PATH = "/home/pi/rv-project/shared/security"

def cipher(message):
    public_file = open(PATH+"/public.key", "r")
    public_key = importKey(public_file.read())
    public_file.close()
    encrypted = public_key.encrypt(message, 32)
    return b64encode(encrypted[0])


def decipher(message):
    message = b64decode(message)
    private_file = open(PATH+"/private.key", "r")
    private_key = importKey(private_file.read())
    private_file.close()
    decrypted = private_key.decrypt(message)
    return decrypted


def generate_key():
    random_generator = Random.new().read
    key = generate(1024, random_generator)

    priv_key = key.exportKey('DER')
    pub_key = key.publickey().exportKey('DER')

    private_file = open(PATH+"/private.key", 'w+')
    private_file.write(priv_key)
    private_file.close()

    public_file = open(PATH+"/public.key", 'w+')
    public_file.write(pub_key)
    public_file.close()


if __name__ == "__main__":
    generate_key()

    msg = cipher("example")
    print msg
    print decipher(msg)
