import random
from utils.random_err import gen_rand_err

def write_to_json(msg):
    gen_rand_err()
    pass

def read_from_json():
    # read from json, but fail 50% of the time
    gen_rand_err()
    with open('./data/journal.json') as f:
        print(f.read())
        return 