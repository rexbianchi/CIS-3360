from io import TextIOWrapper
import re
import sys


def encrypt(key: str, plainText: str) -> str:
    keyLength = len(key)
    encryptedCharList = []

    for i, plainChar in enumerate(plainText):
        keyChar_ASCII = ord(key[i % keyLength])
        plainChar_ASCII = ord(plainChar)
        encryptedCharList.append(
            chr(plainChar_ASCII + keyChar_ASCII - ord('a')))

    return "".join(encryptedCharList)


def getProcessedText(file: TextIOWrapper) -> str:
    raw = file.read()
    processed = (re.sub("[^A-Za-z]", "", raw)).lower()
    return processed


def formattedPrint(textToPrint: str):
    n = 80
    length = len(textToPrint)
    linesToDisplay = [textToPrint[i:i+n] for i in range(0, length, n)]

    for line in linesToDisplay:
        print(line)


def main():
    args = sys.argv[1:]

    if len(args) != 2:
        sys.exit("Incorrent numbers of argumnents!")

    keyText = ""
    plainText = ""

    # Reads
    try:
        with open(args[0], "r") as keyFile:
            keyText = getProcessedText(keyFile)

    except IOError:
        sys.exit(args[0] + " not found!")

    # Reads
    try:
        with open(args[1], "r") as textFile:
            plainText = getProcessedText(textFile)

            # Pads plaintext with x up to a length of 512
            plainText += (512 - len(plainText)) * "x"

    except IOError:
        sys.exit(args[0] + " not found!")

    print("\n\nVigenere Key:\n")
    formattedPrint(keyText)

    print("\n\nPlaintext:\n")
    formattedPrint(plainText)

    cipherText = encrypt(keyText, plainText)

    print("\n\nCiphertext:\n")
    formattedPrint(cipherText)


if __name__ == "__main__":
    main()
