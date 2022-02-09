import tkinter as tk
import tkinter.ttk as ttk


def print_tables(d, geometry):
    window = tk.Tk()
    window.geometry(geometry)

    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, expand=1)

    sec = tk.Frame(main_frame)
    sec.pack(fill=tk.X, side=tk.BOTTOM)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    y_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(tk.ALL)))

    second_frame = tk.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    for name_table in d:
        frame = tk.Frame(second_frame)

        tk.Label(frame, text=name_table).pack(side=tk.TOP)

        names, list_data = d[name_table][0], d[name_table][1]
        n = len(list_data[0])
        tree = ttk.Treeview(frame, show="headings", columns=tuple("#{0!s}".format(i) for i in range(1, len(names)+1)),
                            height=n)
        for i, name in enumerate(names, 1):
            tree.heading("#{0!s}".format(i), text=name)
        for i in range(0, n):
            tree.insert(parent="", index=tk.END, values=tuple(str(list_data[j][i]) for j in range(0, len(names))))
        tree.pack(side=tk.BOTTOM)

        frame.pack()

    window.mainloop()
