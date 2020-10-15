from random import randint
import helper
import numpy as np
import math

'''
    Generator Matrix for Hamming(7, 4)
'''
G4 = [[1, 1, 0, 1],
      [1, 0, 1, 1],
      [1, 0, 0, 0],
      [0, 1, 1, 1],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

'''
    Generator Matrix for Hamming(15, 11)
'''
G11 = [[1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

'''
    Parity Generator Matrix for Hamming(7, 4)
'''
H4 = [[1, 0, 1, 0, 1, 0, 1],
      [0, 1, 1, 0, 0, 1, 1],
      [0, 0, 0, 1, 1, 1, 1]]

'''
    Parity Generator Matrix for Hamming(15, 11)
'''
H11 = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
       [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]]

'''
    Decoder Matrix for Hamming(7, 4)
'''
R4 = [[0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 1]]

'''
    Decoder Matrix for Hamming(15, 11)
'''
R11 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

def HammingCodeDriver():
    mode = input("Enter mode: ")
    total_bits, num_data_bits = (15, 11) if mode == "H1511" else (7, 4)

    message = np.array(helper.generate_random_message(num_data_bits))
    print("Message          :", message)

    x = helper.encodeMessage(G11, message) if total_bits == 15 else helper.encodeMessage(G4, message)
    print("Send Vector      :", x)

    # Create error
    helper.generate_error(x, total_bits)

    z = helper.generateParityCheckMatrix(H11, x) if total_bits == 15 else helper.generateParityCheckMatrix(H4, x)
    print("Received Message :", x)

    print("Parity Check     :", z)

    # Convert to Big endian
    z = z[::-1]

    if sum(z) == 0:
        print("Decoded Message  :", helper.decodeMessage(R11, x)) if total_bits == 15 else print("Decoded Message  :", helper.decodeMessage(R4, x))
    else:
        x = helper.errorCorrection(x, z)
        print("Corrected Message:", x)
        print("Decoded Message  :", helper.decodeMessage(R11, x)) if total_bits == 15 else print("Decoded Message  :", helper.decodeMessage(R4, x))

"""
    Start of Testing Functions
"""

"""
    Function to test successful conversion of syndrome vector to decimal
    Step 1: Convert 'i' to a string of binary numbers and save each digit in a 
            list
    Step 2: Convert the list into a decimal integer (As used in the main script)
    Step 3: Check for successful conversion
"""
def ConvertSyndromeVectorToDecimal(print_results):
    flag = True
    for i in range(0, 16):
        if flag:
            binNum = [int(s) for s in str(bin(i))[2:].split(",")]
            #print(binNum)
            num = int("".join([str(a) for a in binNum]), 2)
            if num != i:
                print("Test ", i, " failed")
                flag = False
            if not flag:
                print("Test ", i, " Failed")
                break
            print("Test ", i, ": SUCCESS")
    if flag and print_results:
        print("Converting Syndrome Vector to Decimal: SUCCESS")

"""
    Tests For Hamming(7, 4)
"""

"""
    Function to check for successful encoding of data bits upto 4 bits
    Step 1: Convert integer to a list of bits to be used as data bits
    Step 2: Generate a syndrome vector by multiplying the message array
            with a generator matrix
    Step 3: Generate a parity check matrix (Sum(z) should always be 0)
    Step 4: Decode the original message using a decoder matrix 
"""
def Hamming74NoError(print_results):
    flag = True
    for i in range(0, 16):
        flag = True
        if print_results: print("Num: ",i)
        message = np.array([int(a) for a in list(bin(i)[2:].zfill(4))])
        x = helper.encodeMessage(G4, message)
        if print_results: print("Message: ",message)
        z = helper.generateParityCheckMatrix(H4, x)[::-1]
        if print_results: print("Parity: ", z)
        if sum(z) == 0:
            if message.all() != helper.decodeMessage(R4, x).all():
                flag = False
        if not flag:
            print("Failed Test: ",i)
            break
    if flag:
        print("Hamming(7, 4) No Errors: SUCCESS")

"""
    Function to check for successful encoding of data bits upto 4 bits
    Step 1: Convert integer to a list of bits to be used as data bits
    Step 2: Generate a syndrome vector by multiplying the message array
            with a generator matrix
    Step 3: Generate an error at each of the bits every iteration 
    Step 4: Generate a parity check matrix
    Step 5: Correct the error 
    Step 5: Decode the original message using a decoder matrix 
"""
def Hamming74WithError(print_results):
    flag = True
    for i in range(0, 16):
        for error_location in range(0,7):
            flag = True
            if print_results: print("Num: ",i, "Error location: ", error_location)
            message = np.array([int(a) for a in list(bin(i)[2:].zfill(4))])
            if print_results: print("Message: ",message)
            x = helper.encodeMessage(G4, message)
            if print_results: print("Syndrome: ", x)
            helper.flip_bit(x, error_location)
            if print_results: print("Syndrome we: ", x)
            z = helper.generateParityCheckMatrix(H4, x)[::-1]
            if print_results: print("Parity: ", z)
            x = helper.errorCorrection(x, z)
            if print_results: print("Fixed Syndrome: ", x)
            if sum(z) == 0:
                if message.all() != helper.decodeMessage(R4, x).all():
                    flag = False
            if not flag:
                print("Failed Test: ",i)
                break
    if flag:
        print("Hamming(7, 4) with Errors: SUCCESS")

"""
    Testing for Hamming(15,11)
"""

"""
    Function to check for successful encoding of data bits upto 11 bits
    Step 1: Convert integer to a list of bits to be used as data bits
    Step 2: Generate a syndrome vector by multiplying the message array
            with a generator matrix
    Step 3: Generate a parity check matrix (Sum(z) should always be 0)
    Step 4: Decode the original message using a decoder matrix 
"""
def Hamming1511NoError(print_results):
    flag = True
    for i in range(0, 2048):
        flag = True
        if print_results: print("Num: ",i)
        message = np.array([int(a) for a in list(bin(i)[2:].zfill(11))])
        x = helper.encodeMessage(G11, message)
        if print_results: print("Message: ",message)
        z = helper.generateParityCheckMatrix(H11, x)[::-1]
        if print_results: print("Parity: ", z)
        if sum(z) == 0:
            if message.all() != helper.decodeMessage(R11, x).all():
                flag = False
        if not flag:
            print("Failed Test: ",i)
            break
    if flag:
        print("Hamming(15, 11) No Errors: SUCCESS")

"""
    Function to check for successful encoding of data bits upto 11 bits
    Step 1: Convert integer to a list of bits to be used as data bits
    Step 2: Generate a syndrome vector by multiplying the message array
            with a generator matrix
    Step 3: Generate an error at each of the bits every iteration 
    Step 4: Generate a parity check matrix
    Step 5: Correct the error 
    Step 5: Decode the original message using a decoder matrix 
"""
def Hamming1511WithError(print_results):
    flag = True
    for i in range(0, 2048):
        for error_location in range(0,15):
            flag = True
            if print_results: print("Num: ",i, "Error location: ", error_location)
            message = np.array([int(a) for a in list(bin(i)[2:].zfill(11))])
            if print_results: print("Message: ",message)
            x = helper.encodeMessage(G11, message)
            if print_results: print("Syndrome: ", x)
            helper.flip_bit(x, error_location)
            if print_results: print("Syndrome we: ", x)
            z = helper.generateParityCheckMatrix(H11, x)[::-1]
            if print_results: print("Parity: ", z)
            x = helper.errorCorrection(x, z)
            if print_results: print("Fixed Syndrome: ", x)
            if sum(z) == 0:
                if message.all() != helper.decodeMessage(R11, x).all():
                    flag = False
            if not flag:
                print("Failed Test: ",i)
                break
    if flag:
        print("Hamming(15, 11) with Errors: SUCCESS")

def runTests():
    print_results = False
    mode = input("Do you want to print the results? [Y/N]")
    if mode == 'Y' or mode == 'y':
        print_results = True
    flag = input("Do you want to run tests for ConvertSyndromeVectorToDecimal function? [Y/N] ")
    if flag == 'Y' or flag == 'y': ConvertSyndromeVectorToDecimal(print_results)
    flag = input("Do you want to run tests for Hamming74NoError function? [Y/N] ")
    if flag == 'Y' or flag == 'y': Hamming74NoError(print_results)
    flag = input("Do you want to run tests for Hamming74WithError function? [Y/N] ")
    if flag == 'Y' or flag == 'y': Hamming74WithError(print_results)
    flag = input("Do you want to run tests for Hamming1511NoError function? [Y/N] ")
    if flag == 'Y' or flag == 'y': Hamming1511NoError(print_results)
    flag = input("Do you want to run tests for Hamming1511WithError function? [Y/N] ")
    if flag == 'Y' or flag == 'y': Hamming1511WithError(print_results)

"""
    End of Testing Functions
"""

def main():

    # For testing, uncomment the following line
    runTests()

    # For running the script in normal mode, uncomment the following line
    #HammingCodeDriver()

if __name__ == "__main__":
    main()