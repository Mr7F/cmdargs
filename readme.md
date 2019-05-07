# cmdargs
## Introduction
Parse the arguments from the command line with just a `decorator`.

The help message is built from the docstring.

## Main
You can use the `@console` decorator on the `main` function, to specify general parameters.

When you will call `parse_args`, the main function will be called, with the parameters.

```python
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
    parse_args()
```

Help message,
> main.py --help

```
usage: main.py [-h] -n  [-a]

Arguments:
  -h, --help    show this help message and exit
  -n , --name   Name of the person
  -a , --age    (18) Age of the person
```

## Multiples functions
You can also use the decorator on multiple functions.

Each function can be called from the command line.
```python
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
    parse_args()
```

General help,
> main.py --help

```
usage: main.py [-h] {sum,product} ...

Modes:
  {sum,product}

Optional arguments:
  -h, --help     show this help message and exit
```

Function help,
> main.py sum --help

```
usage: main.py sum [-h] -a  [-b]

Sum a and b and print the result

Arguments:
  -h, --help  show this help message and exit
  -a , --a    First integer
  -b , --b    (5) Second integer
```

Call a function
> main.py product -a 5 -b 8

```
Result: 40
```
