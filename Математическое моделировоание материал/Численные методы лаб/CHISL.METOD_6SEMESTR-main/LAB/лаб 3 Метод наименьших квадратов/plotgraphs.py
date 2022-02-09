import matplotlib.pyplot as plt
import sys


def show_graph(x, functions, colors):
    fig, ax = plt.subplots()
    if len(functions) != len(colors):
        return
    for key in functions:
        ax.plot(x, functions[key], color=colors[key], label=key)
    ax.set_xlabel("x")  # подпись горизонтальной оси х
    ax.set_ylabel("y")  # подпись вертикальной оси y
    ax.legend()  # показывать условные обозначения
    plt.show()


def print_table(file=sys.stdout, **d):
    for key in d:
        print('{0}: {1}'.format(key, d[key]), file=file)
