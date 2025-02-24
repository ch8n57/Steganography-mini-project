from encrypt import encrypt
from decrypt import decrypt

msg = input("Enter secret message:")

(img, password) = encrypt(msg)

message = decrypt(img, password, len(msg))
if message:
    print("Decrypted message is ", message)
else:
    print("Wrong Password. Please try again")


