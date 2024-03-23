def gen_fibon(n):

    for i in range(n):
        yield i**2
        


for number in gen_fibon(10):
    print(number)