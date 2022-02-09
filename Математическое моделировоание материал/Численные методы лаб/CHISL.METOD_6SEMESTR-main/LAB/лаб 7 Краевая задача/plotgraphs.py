import matplotlib.pyplot as plt


def show_graph(arr_x, functions, colors):
    fig, ax = plt.subplots()
    if len(functions) != len(colors) or len(arr_x) != len(colors):
        return
    for key in functions:
        ax.plot(arr_x[key], functions[key], color=colors[key], label=key)
    ax.set_xlabel("x")  # подпись горизонтальной оси х
    ax.set_ylabel("y")  # подпись вертикальной оси y
    ax.legend()  # показывать условные обозначения
    plt.show()
