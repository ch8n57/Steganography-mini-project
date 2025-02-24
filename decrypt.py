
def decrypt(img, password, msg_length):
    message = ""
    n = 0
    m = 0
    z = 0

    c = {}
    for i in range(255):
        c[i] = chr(i)

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        for i in range(msg_length):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        return message
    else:
        return False

