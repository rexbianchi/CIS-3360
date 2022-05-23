"""
+=============================================================================
| Assignment: pa02 - Calculating an 8, 16, or 32 bit
| checksum on an ASCII input file
|
| Author: Rex Bianchi
| Language: Python
|
| To Compile: javac pa02.java
| gcc -o pa02 pa02.c
| g++ -o pa02 pa02.cpp
| go build pa02.go
| python pa02.py //Caution - expecting input parameters
|
| To Execute: java -> java pa02 inputFile.txt 8
| or c++ -> ./pa02 inputFile.txt 8
| or c -> ./pa02 inputFile.txt 8
| or go -> ./pa02 inputFile.txt 8
| or python-> python pa02.py inputFile.txt 8
| where inputFile.txt is an ASCII input file
| and the number 8 could also be 16 or 32
| which are the valid checksum sizes, all
| other values are rejected with an error message
| and program termination
|
| Note: All input files are simple 8 bit ASCII input
|
| Class: CIS3360 - Security in Computing - Spring 2022
| Instructor: McAlpin
| Due Date: per assignment
|
+=============================================================================
"""
import sys

VALID_CHECKSUM_SIZES = [8, 16, 32]


def calculateCheckSum(message: str, checkSumSize: int) -> int:
    checkSum = 0  # Stores final checkSum to be returned
    wordSize = checkSumSize // 8
    bitmask = 2**checkSumSize - 1  # Bitmask to ignore overflow

    word = 0
    shift = wordSize
    for i in message:
        shift -= 1
        word += ord(i) << (8 * shift)

        if shift == 0:
            # Add word to final checkSum and discard overflow
            checkSum += word
            checkSum &= bitmask

            # Reset word and shift
            word = 0
            shift = wordSize

    return checkSum


def main():
    args = sys.argv[1:]

    if len(args) != 2:
        sys.stderr.write("Incorrect number of arguments.\n")
        return

    fileName = args[0]
    checkSumSize = int(args[1])

    # Tries to open the input file
    try:
        inFile = open(fileName, "r")
    except FileNotFoundError:
        sys.stderr.write(fileName + " not found. Please check the file name.\n")
        return

    # Checks to see if checkSumSize is valid
    try:
        VALID_CHECKSUM_SIZES.index(checkSumSize)
    except ValueError:
        sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
        return

    fileContents = inFile.readline()

    # Pads with X if needed
    while (len(fileContents) % (checkSumSize / 8)) != 0:
        fileContents += "X"

    # Prints 80 chars per line
    print("")
    for i, letter in enumerate(fileContents, 1):
        print(letter, end="")
        if i % 80 == 0:
            print("")
    print("")

    checkSum = calculateCheckSum(fileContents, checkSumSize)

    print(
        f"{checkSumSize:2} bit checksum is {hex(checkSum)[2:]:>8} for all{len(fileContents):4} chars"
    )


if __name__ == "__main__":
    main()

"""
==============================================================================
| I [Rex Bianchi] ([re322774]) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+=============================================================================
"""
