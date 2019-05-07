from cmdargs import console, parse_args


@console
def main(name, age: int = 18):
    '''
    Args:
        name: Name of the person
        age: Age of the person
        sex: 'm' or 'f'
    '''
    print('Name:', name)
    print('Age:', age)


if __name__ == '__main__':
    import sys
    sys.argv = ['main.py', '-s']
    parse_args()
