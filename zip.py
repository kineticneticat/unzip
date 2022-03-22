import pickle
from sys import argv

try:
    inp = open(argv[1], 'rb')
    file = argv[1]
except IndexError:
        try:
            file = str(input('file:\n'))
        except FileNotFoundError as err:
            raise FileNotFoundError
filename = file.split('.')[0]
filetype = file.split('.')[1]

with open(file, 'rb') as inp:
    inp = pickle.load(inp)
    print(inp)
    open(f'{filename}.{filetype}', 'wb').write(inp['data'])