with open("inputs/day_7.data") as file:
    lines = [line.rstrip() for line in file]

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory():
    def __init__(self, name):
        self.name = name
        self.dirs = []
        self.files = []
        self.size = 0
        self.parent = None

    def __repr__(self):
        return f"<DIR> {self.name} - {self.size} - {', '.join(map(lambda d: d.name, self.dirs))} - {', '.join(map(lambda f: f.name, self.files))}"

    def add_directory(self, dir):
        if any(dir.name == d.name for d in self.dirs):
            return

        self.dirs.append(dir)
        dir.parent = self

    def get_directory(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return dir

        return None

    def add_file(self, file):
        if any(file.name == f.name for f in self.files):
            return

        self.files.append(file)
        self.size += file.size
        _d = self
        while _d.parent is not None:
            _d = _d.parent
            _d.size += file.size


root = Directory('/')

current = root
i = 0
while True:
    if i >= len(lines):
        break

    line = lines[i]

    if line == '$ cd /':
        current = root
        i += 1

    elif line == '$ cd ..':
        current = current.parent
        i += 1

    elif line[0:5] == '$ cd ':
        current = current.get_directory(line[5:])
        i += 1

    elif line == '$ ls':
        while True:
            i += 1
            if i >= len(lines):
                break

            line = lines[i]
            if line[0] == '$':
                break

            if line[0:3] == 'dir':
                current.add_directory(Directory(line[4:]))
            else:
                size, name = line.split(' ')
                size = int(size)
                current.add_file(File(name, size))

    else:
        raise ValueError("Unknown command")


# Part 1
res = 0
to_check = [root]
while len(to_check) > 0:
    d = to_check.pop()
    if d.size <= 100000:
        res += d.size
    for dd in d.dirs:
        to_check.append(dd)


print(res)


