from random import randint

def generate_random_message(num_data_bits):
      message = []
      for i in range(num_data_bits):
          message.append(randint(0, 1))
      return message

def generate_error(x, total_bits):
      chance_of_error = (randint(0, total_bits))
      print(chance_of_error)
      if chance_of_error > 0:  
        loc = randint(1, total_bits);
        flip_bit(x, loc)
      return
  
def flip_bit(x, loc):
      x[loc - 1] = 1 - x[loc - 1]
      return
