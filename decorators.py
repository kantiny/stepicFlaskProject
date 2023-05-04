"""
Создайте декоратор, который будет проверять значение на уникальность аргументы
"""


def controller(func):
    args = []

    def wrapper(arg):
        if arg not in args:
            args.append(arg)
            func(arg)
        else:
            print('This arg - {} already exist'.format(arg))
    return wrapper


@controller
def hello(tmp):
    print('hello, {}'.format(tmp))


hello('a')
hello('b')
hello('a')
