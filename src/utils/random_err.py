import random
def gen_rand_err():
    num = random.random()
    print('num: ', num)
    if num<0.7:
        print('err')
        raise FileExistsError