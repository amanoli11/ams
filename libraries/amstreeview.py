import tkinter as tk
from tkinter import Menu, StringVar, Toplevel, ttk
import csv
from tkinter import messagebox

def AMSTreeVIew(parent, table_column, table_values, frame_name = "TABLE", table_height = 10):


    parent_for_filter = parent

    table_column_for_filter = table_column

    lf = ttk.LabelFrame(parent, text=frame_name)
        # lf = ttk.LabelFrame(parent, text=frame_name, labelanchor= "n")

    tree = ttk.Treeview(lf, columns=table_column, show='headings', height=table_height)

    def write_to_csv(value):
        with open("excel_export.csv", "w") as f:
            w = csv.writer(f, dialect='excel')
            for record in value:
                w.writerow(record)

        messagebox.showinfo("COMPLETE!!!", "Table Exported Successfully.")


    options = Menu(tree, tearoff=False)
    options.add_command(label="EXPORT TO EXCEL", command=lambda: write_to_csv(table_values))

    def option_menu(event):
        options.tk_popup(event.x_root, event.y_root)


    tree.bind("<Button-3>", option_menu)


    # csv_button = ttk.Button(lf, text="EXPORT TO EXCEL", command=lambda: write_to_csv(table_values))
    # csv_button.grid(row=0, column=0, sticky=tk.NE)

    for i in table_column:
        tree.heading(str(i), text = str(i))

    tree.tag_configure('oddcolumn', background='white')
    tree.tag_configure('evencolumn', background='lightblue')

    AMSStripedRows(tree, table_values)


    tree.grid(row=1, column=0, padx=(10,0), pady=10)

    parent.scrollbar = ttk.Scrollbar(lf, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=parent.scrollbar.set)
    parent.scrollbar.grid(row=1, column=1, sticky='ns')


    # if filter:
    #     filter_table(tree, parent, table_column, options)

    return lf, tree, options


def AMSStripedRows(tree, table_values):
    count = 0


    for i in table_values:
        if count % 2 == 0:
            tree.insert('', tk.END, values=i, tags='oddcolumn')
        else:
            tree.insert('', tk.END, values=i, tags='evencolumn')
        count += 1



# def filter_table():

#     row_count = 0
#     new_filter_window = Toplevel(parent_for_filter)
#     new_filter_window.title("Filter Table Window")


#     string_array = []

#     for i in table_column_for_filter:

#         filter_label = tk.Label(new_filter_window, text=i)
#         filter_label.grid(row=row_count, column=0, padx=10, pady=10, sticky=tk.NW)

#         filter_entry = tk.Entry(new_filter_window)
#         filter_entry.grid(row=row_count, column=1, padx=10)

#         row_count += 1

#         string_array.append(filter_entry)

#     parent_for_filter.filter_val = string_array
#     parent_for_filter.filter_window = new_filter_window


# def filter_table():

#     def filter_window():
#         row_count = 0
#         new_filter_window = Toplevel(parent_for_filter)
#         new_filter_window.title("Filter Table Window")


#         string_array = []

#         for i in table_column_for_filter:

#             filter_label = tk.Label(new_filter_window, text=i)
#             filter_label.grid(row=row_count, column=0, padx=10, pady=10, sticky=tk.NW)

#             filter_entry = tk.Entry(new_filter_window)
#             # filter_entry.bind("<KeyRelease>", get_value)
#             filter_entry.grid(row=row_count, column=1, padx=10)

#             row_count += 1

#             string_array.append(filter_entry)

#         parent_for_filter.filter_val = string_array

#     options.add_separator()
#     options.add_command(label="Filter", command=filter_window)