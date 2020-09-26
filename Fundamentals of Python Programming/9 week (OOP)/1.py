from copy import deepcopy
from sys import stdin


class Matrix(list):
    def __init__(self, dim_list):
        self.dim_list = [line.copy() for line in dim_list]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.dim_list])

    def size(self):
        return len(self.dim_list), len(self.dim_list[0])


exec(stdin.read())
