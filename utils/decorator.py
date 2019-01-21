# decorator functions

import functools



class NiceDecorator(object):
    def __init__(self, param_foo='a', param_bar='b'):
        self.param_foo = param_foo
        self.param_bar = param_bar

    def __call__(self, func):
        @functools.wraps(func)
        def my_logic(*args, **kwargs):
            # whatever logic your decorator is supposed to implement goes in here
            print('pre action baz')
            print(self.param_bar)
            print(self.param_foo)
            # including the call to the decorated function (if you want to do that)
            result = func(*args, **kwargs)
            print('post action beep')
            return result

        return my_logic


NiceDecorator2 = NiceDecorator(param_foo='changed2!', param_bar='baaar2')


# usage example from here on
@NiceDecorator2
def example():
    print('example yay')




if __name__ == '__main__':
    example()
