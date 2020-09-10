import numpy as np
import random
import math

G = [[1, 1, 0, 1],
     [1, 0, 1, 1],
     [1, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]

H = [[1, 0, 1, 0, 1, 0, 1],
     [0, 1, 1, 0, 0, 1, 1],
     [0, 0, 0, 1, 1, 1, 1]]

R = [[0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1]]

mode = input("Enter mode: ")
message = input("Enter Message: ").split()
message = list(map(int, message))
print("Message : ",message)

x = np.matmul(G, message) % 2
print("Send vector: ",x)

z = np.matmul(H, x) % 2
print("Received message: ",x)
print("Parity Check: ",z)
p = np.matmul(R, x)
print("Decoded message: ",p)
