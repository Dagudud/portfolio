import random
def generate_password(lowercase, numbers, uppercase, symbols):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    upperalphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sym = '!@#$%^&*_'
    password = []
    if lowercase == True:
        for i in range(4):
            x = random.choice(alphabet)
            password.append(x)
    if numbers == True:
        for i in range(4):
            y = random.choice(num)
            password.append(y)
    if uppercase == True:
        for i in range(4):
            z = random.choice(upperalphabet)
            password.append(z)
    if symbols == True:
        for i in range(4):
            a = random.choice(sym)
            password.append(a)
    random.shuffle(password)
    password = ''.join(password)
    return password