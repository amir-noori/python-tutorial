
#Cryptography Challenge #1 - www.101computing.net/cryptography-challenge-1/
import random, time


'''
Your first task is to reverse-engineer this code to understand how this encryption 
algorithm works. Then, your challenge consists of writing a new function called
decrypt(), that takes two parameters (a ciphertext and a key) and returns 
the plaintext corresponding to the given ciphertext.

decrypt these:
  HNABntvVepMaQSNHyKxQTXZf HVbQXcqJSXfswOAuRBzpefOdfBeylimeqDHDlFc
  PqKgakYBpfzveAHVrrUgbzpkaMWUcskukxac QfsWpFSrTrwiaQRtSsXesGlrBqv
  PHcRrveeRUmDnfqMFAnBJvvwyzSDrj tqXhrLRXIegaDLwdInIGCvqelcjzU
'''


#A basic encryption algorithm...
def encrypt(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ciphertext = ""
  for i in range(0,len(plaintext)):
    character = plaintext[i]
    ciphertext = ciphertext + character
    for j in range (0,key):
      ciphertext = ciphertext + random.choice(alphabet)
  return ciphertext


def decrypt1(enplaintext, enkey):
  mystring = enplaintext
  ciphertext = ""
  while len(mystring) != 0:
    character = mystring[0]
    ciphertext = ciphertext + character
    mystring = mystring[1 + enkey:len(mystring)]
  return ciphertext


def decrypt2(ciphertext, key):
  plaintext = ""
  counter = 0
  for c in ciphertext:
    if counter == 0:
      plaintext += c
      counter += 1
    elif counter == key:
      counter = 0
    else:
      counter += 1
      
  return plaintext


def decrypt3(ciphertext, key):
  return "".join([c for c in ciphertext[0::(key+1)]])

plaintext = "test text"
key = 2
ciphertext = encrypt(plaintext, key)
print(ciphertext)
decrypted_result1 = decrypt1(ciphertext, key)
print(decrypted_result1)
decrypted_result2 = decrypt2(ciphertext, key)
print(decrypted_result2)
decrypted_result3 = decrypt3(ciphertext, key)
print(decrypted_result3)
