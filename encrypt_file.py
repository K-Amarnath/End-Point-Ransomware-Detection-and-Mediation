import rsa

def loadKeys():
    pkey = open('pub_key', 'rb')
    publicKey = rsa.PublicKey.load_pkcs1(pkey.read())
#    privkey  = open('priv_key', 'rb')
#    privateKey = rsa.PrivateKey.load_pkcs1(priv.key.read())
    return publicKey

sensitive_file =  open('sensitive.txt', 'rb')
message = sensitive_file.read()

#message = message_unencoded.encode('utf-8')

def encrypt(message, key):
  result = []
  for n in range(0,len(message),373):
      part = message[n:n+373]
      result.append(rsa.encrypt(part, key))
  #print(len(result),len(result[0]))
  ciphertext = b''.join(result)
  encrpted_file = open('sensitive.txt','wb')
  encrpted_file.write(ciphertext)

encrypt(message,loadKeys())