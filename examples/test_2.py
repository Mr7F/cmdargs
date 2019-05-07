from cmdargs import console, parse_args


@console
def sum(a: int, b: int = 5):
    '''
    Sum a and b and print the result

    Args:
        a: First integer
        b: Second integer
    '''
    print('Result:', a + b)


@console
def product(a: int, b: int = 5):
    '''
    Multiply a and b and print the result

    Args:
        a: First integer
        b: Second integer
    '''
    print('Result:', a * b)


if __name__ == '__main__':
    import sys
    sys.argv = ['main.py', 'product', '-a', '5', '-b', '8']
    parse_args()
