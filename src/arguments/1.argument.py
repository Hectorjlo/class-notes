import sys 

# print(sys.argv)
print('')
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f'Hello {name}, welcome')
else: 
    print('Name required')

print('')