from cmdargs import console


@console
def product(a, b=5):
    print(a * b)
