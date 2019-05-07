import sys
from cmdargs import console, parse_args


@console
def main(person_name, age: int = 18, sex='m', ok: bool = True):
    '''
    Show information about the person

    Args:
        person_name: Name of the person
        age: Age of the person
        sex: 'm' or 'f'
    '''
    print('Name:', person_name)
    print('Age:', age)
    print('OK:', ok)


if __name__ == '__main__':
    sys.argv = ['main.py', '--person_name', 'Mister7F', '--a', '23']
    parse_args()
    print('\nCommand: ', ' '.join(sys.argv))
