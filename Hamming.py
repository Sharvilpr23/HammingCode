from random import randint
import helpers
import numpy as np
import math

G4 = [[1, 1, 0, 1],
      [1, 0, 1, 1],
      [1, 0, 0, 0],
      [0, 1, 1, 1],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]
  
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
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]];

H4 = [[1, 0, 1, 0, 1, 0, 1],
      [0, 1, 1, 0, 0, 1, 1],
      [0, 0, 0, 1, 1, 1, 1]];
  
H11 = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
       [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0 ,0, 1, 1, 1, 1, 1, 1, 1, 1]];
  
R4 = [[0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 1]];
  
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
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]];

mode = input("Enter mode: ")

if mode == 'H74':
    total_bits = 7
    num_data_bits = 4
elif mode == 'H1511':
    total_bits = 15
    num_data_bits = 11

message = np.array(helpers.generate_random_message(num_data_bits))

print("Message          :",message)
if total_bits == 7:
    x = np.matmul(G4, message) % 2
elif total_bits == 15:
    x = np.matmul(G11, message) % 2

print("Send Vector      :",x)

#Create error
helpers.generate_error(x, total_bits)

if total_bits == 7:
    z = np.matmul(H4, x) % 2
else:
    z = np.matmul(H11, x) % 2

print("Received Message :",x)
print("Parity Check     :",z)

#Convert to Big endian
z = z[::-1]
if sum(z) == 0:
    print("Decoded Message  :",np.matmul(R4, x))
else:
    error_location = int("".join([str(a) for a in z]), 2)
    helpers.flip_bit(x, error_location)
    print("Corrected Message:",x)
    if total_bits == 7:
        decode = np.matmul(R4, x)
    else:
        decode = np.matmul(R11, x)
    print("Decoded Message  :",decode)

