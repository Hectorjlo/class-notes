import sys

try:
    if len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        print(f'The sum is: {a + b}')

    else:
        print('Two values are required')
except Exception:
    print('Only numbers are permited')