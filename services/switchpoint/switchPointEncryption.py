import time
import numpy as np
from itertools import cycle

def constructKey(seedValue):
    np.random.seed(int(seedValue))
    x = np.prod(np.random.randint(1, 100, 10))
    print("X: {}".format(x))
    return x


def encrypt(plainText, cipher):
    cipherString = str(cipher)
    return ''.join(chr(ord(c)^ord(k)) for c,k in zip(plainText, cycle(cipherString)))

def newCrypt(cipherText, timeStamp):
    oldKey = constructKey(timeStamp)
    newKey = constructKey(time.time())
    # diffKey = oldKey^newKey
    diffKey = encrypt(str(oldKey), str(newKey))
    oldCipher = encrypt(cipherText, oldKey)
    diffCipher = encrypt(oldCipher, diffKey)
    plain = encrypt(diffCipher, newKey)
    print("Old Key: {}".format(oldKey))
    print("Diff Key: {}".format(diffKey))
    # print("LDK {}".format(len(diffKey)))
    print("New Key: {}".format(newKey))


    print("Cipher: {}".format(cipherText))
    print("Old Cipher: {}".format(oldCipher))
    print("Diff Cipher: {}".format(diffCipher))
    print("Plain: {}".format(plain))
    print(plain==cipherText)



def main():
    strT ="whyisntthiswork?whyisntthiswork?"
    print(len(strT))
    newCrypt(strT, 500)


if __name__ == '__main__':
    main()
