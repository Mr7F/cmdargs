from cmdargs import console, parse_args


class MyClass:
    @staticmethod
    @console
    def method(i: int = 1):
        print('i = ', i)


if __name__ == '__main__':
    import sys
    sys.argv = ['main.py', 'method']
    parse_args()
