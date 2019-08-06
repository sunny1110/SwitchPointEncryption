import time
import numpy as np
import sys
from itertools import cycle


def constructKey(seedValue):
    np.random.seed(int(seedValue))
    x = np.random.randint(1000000, 9999999)
    print("X: {}".format(x))
    return x


def encrypt(plainText, cipher):
    cipherString = str(cipher)
    return ''.join(chr(ord(c)^ord(k)) for c,k in zip(plainText, cycle(cipherString)))

def reCrypt(cipherText, timeStamp):
    oldKey = constructKey(timeStamp)
    now = int(time.time())
    newKey = constructKey(now)
    # diffKey = oldKey^newKey
    diffKey = encrypt(str(oldKey), str(newKey))
    oldCipher = encrypt(cipherText, oldKey)
    diffCipher = encrypt(oldCipher, diffKey)
    plain = encrypt(diffCipher, newKey)
    print("Old Key: {}".format(oldKey))
    print("Diff Key: {}".format(diffKey))
    print("LDK {}".format(len(diffKey)))
    print("New Key: {}".format(newKey))


    print("Cipher: {}".format(cipherText))
    print("Old Cipher: {}".format(oldCipher))
    print("Diff Cipher: {}".format(diffCipher))
    print("Plain: {}".format(plain))
    # print(plain==cipherText)
    returnObject = {}
    returnObject["updated"] = now
    returnObject["password"] = diffCipher
    return returnObject

def newCrypt(plain, timeStamp):
    key = constructKey(timeStamp)
    cipherText = encrypt(plain, key)
    return cipherText




def main():
    strT = sys.argv[1]
    print(len(strT))
    reCrypt(strT, np.random.randint(0, 20000))


if __name__ == '__main__':
    main()
