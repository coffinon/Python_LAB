import os


def tree(directory, depth):
    elements = os.listdir(directory)
    for element in elements:
        path = os.path.join(directory, element)
        print(depth * "   " + element)
        if os.path.isdir(path):
            tree(path, depth + 1)


tree(os.path.dirname(os.path.realpath(__file__)), 0)
