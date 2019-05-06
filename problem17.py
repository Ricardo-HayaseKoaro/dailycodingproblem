def buildPath(str):

    dir = {}
    path = []
    dir_list = str.split("\n")

    for x in dir_list:
        tabs = 0
        while "\t" in x[:2]:
            x = x[1:]
            tabs += 1

        current_item = dir

        for subdir in path[:tabs]:
            current_item = current_item[subdir]

        if '.' in x:
            current_item[x] = True
        else:
            current_item[x] = {}

        path = path[:tabs]
        path.append(x)
        print(path)

    return dir


def longestpath(dir):
    paths = []
    for key, item in dir.items():
        if item is True:
            paths.append(key)
        else:
            paths.append(key + "/" + longestpath(item))

    paths = [path for path in paths if '.' in path]
    if paths:
        return max(paths, key=lambda path: len(path))
    else:
        return '



str = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(buildPath(str))
