alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plaintext, cipher_key):
  to_encrypt = [i for i in plaintext]
  encrypted = ""
  character_num = 0
  for letter in to_encrypt:
    encrypted += chr(ord(letter) + cipher_key)
  return encrypted

def decrypt(ciphertext, cipher_key):
  to_decrypt = [i for i in ciphertext]
  decrypted = ""
  character_num = 0
  for letter in to_decrypt:
    decrypted += chr(ord(letter) - cipher_key)
  return decrypted

def main():
  function = input("Enter e for encrypt, d for decrypt: ")
  if function == "e":
    plaintext = input("Enter the plaintext to encrypt: ")
    cipher = int(input("Enter a cipher key between 1 and 26 inclusive: "))
    while cipher <= 0 or cipher >= 26:
      cipher = int(input("Invalid cipher key. Please enter a valid cipher key: "))
    print(encrypt(plaintext, cipher))
  elif function == "d":
    ciphertext = input("Enter the ciphertext to decrypt: ")
    cipher = int(input("Enter the cipher key between 1 and 26 inclusive: "))
    while cipher <= 0 or cipher >= 26:
      cipher = int(input("Invalid cipher key. Please enter a valid cipher key: "))
    print(decrypt(ciphertext, cipher))
  else:
    print("Invalid function selected")

main()