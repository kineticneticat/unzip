import pickle
from sys import argv

try:
    inp = open(argv[1], 'rb')
    file = argv[1]
except IndexError:
        try:
            file = str(input('file:\n'))
        except FileNotFoundError as err:
            exit('FileNotFound')

def unzip(file):
    filename = file.split('.')[0]
    filetype = file.split('.')[1]
    with open(file, 'rb') as inp:
        data = {
            'filetype': filetype,
            'data': inp.read()
        }
        pickle.dump(data, open(f'{filename}.unzip', 'wb'))

def zip(file):
    with open(file, 'rb') as inp:
        try:
            inp = pickle.load(inp)
        except EOFError:
            exit('No Data')
        print(inp)
        filetype = inp['filetype']
        filename = file.split('.')[0]
        open(f'{filename}.{filetype}', 'wb').write(inp['data'])

if file.split('.')[1] == 'unzip':
    zip(file)
else:
    unzip(file)