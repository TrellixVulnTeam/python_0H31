
import random
import string

def rand_string(length, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = ''.join(random.choice(
                        string.ascii_lowercase 
                        + string.ascii_uppercase 
                        + string.digits)
                   for i in range(length))
    output.put(rand_str)