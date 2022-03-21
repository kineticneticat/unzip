import pickle
from sys import argv

try:
    inp = open(argv[1], 'rb')
    file = argv[1]
except IndexError:
        try:
            file = str(input('file:\n'))
            inp = open(file, 'rb')
        except FileNotFoundError as err:
            raise FileNotFoundError
filename = file.split('.')[0]
print(inp.read())
filetype = pickle.load(inp)['filetype']
out = open(f'{filename}.{filetype}', 'wb')

out.write(pickle.loads(pickle.load(inp)['data']))