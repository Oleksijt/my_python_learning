class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
        print('{} closed'.format(self))

files = []
for _ in range(10):
    with File('foo.txt', 'w') as infile:
        infile.write('foo')
        print(files)
        raise Exception
        files.append(infile)
print(files)