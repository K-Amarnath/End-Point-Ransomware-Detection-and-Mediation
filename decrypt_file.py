import rsa

def loadKeys():
  #   pkey = open('pub_key', 'rb')
  #   publicKey = rsa.PublicKey.load_pkcs1(pkey.read())
  privkey  = open('priv_key', 'rb')
  priv_Key = rsa.PrivateKey.load_pkcs1(privkey.read())
  return priv_Key

encrypted_file =  open('sensitive.txt', 'rb')
message = encrypted_file.read()
#print(message)

#message = message_unencoded.encode('utf-8')

def decrypt(message,key):
    result = []
    for n in range(0,len(message),384):
        part = message[n:n+384]
        result.append( rsa.decrypt(part, key))
    result = b''.join(result)
    plaintext_file = open('sensitive.txt','wb')
    plaintext_file.write(result)
#print(loadKeys())
decrypt(message,loadKeys())