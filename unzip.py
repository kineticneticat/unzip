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
out = open(f'{filename}.unzip', 'wb')


data = {
    'filetype': file.split('.')[1],
    'data' : inp.read()
}
print(data)
pickle.dump(data, out)

inp.close()
out.close()