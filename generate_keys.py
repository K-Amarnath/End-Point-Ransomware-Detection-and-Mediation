# -*- coding: utf-8 -*-
"""Generate_keys

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jn6Jvv9kTZM6RKOc0AwO0pbhcdI3pHU3
"""

import rsa 

def generate_keys():
  (public_key, private_key) = rsa.newkeys(3072)

  with open("pub_key", "wb") as file:
    file.write(public_key.save_pkcs1("PEM"))
    file.close()

  with open("priv_key", "wb") as file:
    file.write(private_key.save_pkcs1("PEM"))
    file.close()

  generate_keys()