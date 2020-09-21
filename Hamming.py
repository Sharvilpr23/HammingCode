import numpy as np
import random
import math

G4 = [[1, 1, 0, 1],
     [1, 0, 1, 1],
     [1, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]
G11 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0,	0, 0, 0],
       [0, 1, 1, 0, 0, 0, 0, 0,	0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0,	0, 0, 0],
       [1, 0, 0, 1, 1, 0, 0, 0,	0, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0,	0, 0, 0],
       [0, 0, 1, 0, 0, 1, 1, 0,	0, 0, 0],
       [0, 0, 0, 1, 0, 0, 1, 1,	0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 1,	1, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0,	1, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0,	0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 1,	0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0,	1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0,	0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0,	0, 0, 1]]

H4 = [[1, 0, 1, 0, 1, 0, 1],
      [0, 1, 1, 0, 0, 1, 1],
      [0, 0, 0, 1, 1, 1, 1]]

H11 = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
       [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0 ,0, 0, 1, 1, 1, 1, 1, 1, 1]]

R4 = [[0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 1]]

R11 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ,0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ]]

mode = list(input("Enter mode: "))

if len(mode) == 3:
    total_bits = int(mode[1])
    num_data_bits = int(mode[2])
else:
    total_bits = int(mode[1] + mode[2])
    num_data_bits = int(mode[3] + mode[4])

def generate_random_message(num_data_bits):
    message = []
    for i in range(num_data_bits):
        temp = random.randint(0, 1)
        message.append(temp)
    return message

message = generate_random_message(num_data_bits)
print("Message           :",message)

if total_bits == 7:
    x = np.matmul(G4, message) % 2
elif total_bits == 15:
    x = np.matmul(G11, message) % 2

print("Send vector       :",x)

def generate_error(x, total_bits):
    loc = random.randint(1, total_bits);
    flip_bit(x, loc)
    return

def flip_bit(x, loc):
    x[loc - 1] = 1 - x[loc - 1]
    return

#Create error
generate_error(x, total_bits)

if total_bits == 7:
    z = np.matmul(H4, x) % 2
else:
    z = np.matmul(H11, x) % 2

print("Received message  :",x)
print("Parity Check      :",z)

if sum(z) == 0:
    print("Decoded message   :",message)
else:
    error_location = int("".join([str(a) for a in z]), 2)
    flip_bit(x, error_location)
    print("Corrected message :",x)
    if total_bits == 7:
        decode = np.matmul(R4, x)
    else:
        decode = np.matmul(R11, x)
    print("Decoded message   :",decode)

