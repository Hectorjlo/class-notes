import argparse

parser = argparse.ArgumentParser(description='This is a probe', epilog='Look at me')
parser.add_argument('name', help='Name of the individual')
parser.add_argument('--age', help='Age of the individual')
parser.add_argument('surname', help='Surname of the individual')
arguments = parser.parse_args()

print(arguments)


print(f'The name of the user is {arguments.name} {arguments.surname} your age is {arguments.age}')
