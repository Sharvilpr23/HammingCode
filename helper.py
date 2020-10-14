from random import randint
import numpy as np

def generate_random_message(num_data_bits):
    message = []
    for i in range(num_data_bits):
        message.append(randint(0, 1))
    return message

def encodeMessage(generator_matrix, message):
    return np.matmul(generator_matrix, message) % 2

def generate_error(x, total_bits):
    chance_of_error = randint(0, total_bits)
    if chance_of_error > 0:
        loc = randint(1, total_bits)
        flip_bit(x, loc)
    return

def generateParityCheckMatrix(parity_generator_matrix, syndrome_vector):
    return np.matmul(parity_generator_matrix, syndrome_vector) % 2

def errorCorrection(syndrome_vector, parity_check_matrix):
    error_location = int("".join([str(bit) for bit in parity_check_matrix]), 2)
    flip_bit(syndrome_vector, error_location)
    return syndrome_vector

def decodeMessage(decoder_matrix, syndrome_vector):
    return np.matmul(decoder_matrix, syndrome_vector) % 2

def flip_bit(x, loc):
    x[loc - 1] = 1 - x[loc - 1]
    return
