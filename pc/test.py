from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode
from base64 import b64decode
import json

key = get_random_bytes(16)
header = b'header'
message = b'le train est kali'

# Encrypt
cipher_key = AES.new(key, AES.MODE_EAX)
cipher_key.update(header)
ciphertext, tag = cipher_key.encrypt_and_digest(message)

json_k = ['nonce', 'header', 'ciphertext', 'tag']
json_v = [b64encode(x).decode('utf-8') for x in (cipher_key.nonce, header, ciphertext, tag)]
result = json.dumps(dict(zip(json_k, json_v)))
print(result)

# Decrypt
jv = {k: k for k in json_k}
print(jv)

cipher = AES.new(key, AES.MODE_EAX, nonce=jv['nonce'])
cipher.update(jv['header'])
plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
print("The message was: " + plaintext.decode('utf-8'))