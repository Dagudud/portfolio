import time

def candy_wrapper(funk):
    def wrap():
        a = funk()
        print('---------------')
        print(a)
        print('---------------')
    return wrap

def stopwatch(funk):
    def wrap():
        start = time.time()
        result = funk()
        end = time.time()
        print(f'Время выполнения функции {round(end - start, 2)} секунд')
    return wrap

@stopwatch
def ask():
    return input('Введите фразу: ')

def controller(funk):
    names = []
    def wrap(x):
        if x in names:
            print('Данный аргумент уже был передан')
        else:
            names.append(x)
            return funk(x)
    return wrap
    
@controller
def hello(name):
    print(f'Привет, {name}')

hello('Вася')
hello('Петя')
hello('Вася')
#ask()