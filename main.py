import random

def my_sqrt(x):
    approx = None
    guess = x/2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

def sqrt_program(arg):
    x = int(arg)
    print('The root of', x, 'is', my_sqrt(x))

# def fuzzer():
#     out =""
#     for i in range (0,5):
#         out += chr(random.randrange(32,64))
#     return out

def fuzzer(max_length=100, char_start=32, char_range=32):
    string_length = random.randrange(0, max_length+1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

if __name__ == '__main__':
    print(fuzzer())
    