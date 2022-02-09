import sys

from prettytable import PrettyTable


def print_table(name_columns, data, file=sys.stdout):
    n, table = len(name_columns), PrettyTable(name_columns)
    while data:
        table.add_row(data[:n])
        data = data[n:]
    print(table, file=file)


def print_constants(file=sys.stdout, **d):
    for key in d:
        print('{0} = {1!s}'.format(key, d[key]), file=file)


def getData(arr_columns):
    data = list()
    for i in range(0, len(arr_columns[0])):
        data += [column[i] for column in arr_columns]
    return data
