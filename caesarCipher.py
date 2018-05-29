plaintext=input("plaintext?")
shift=int(input("shift?"))
ciphertext=""
for letter in plaintext:
    pos = ord(letter) # what is the ascii code?
    newpos = pos + shift  # add the shift
    ciphertext = ciphertext + chr(newpos) # append new char
print("ciphertext=",ciphertext)
