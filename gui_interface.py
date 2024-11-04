import tkinter as tk
from tkinter import ttk

FONT = None  # ("arial", 24)
PADDING = 5


def main_window():

    root = tk.Tk()
    root.title("Blood Database")
    # root.geometry("800x800")

    title_label = ttk.Label(root, text="Blood Donor Database", font=FONT)
    title_label.grid(column=0, row=0, columnspan=2, sticky=tk.W,
                     padx=PADDING, pady=PADDING)

    name_label = ttk.Label(root, text="Name:", font=FONT)
    name_label.grid(column=0, row=1, sticky=tk.E, padx=PADDING, pady=PADDING)
    name_entry = ttk.Entry(root, font=FONT)
    name_entry.grid(column=1, row=1, padx=PADDING, pady=PADDING)

    id_label = ttk.Label(root, text="Id:", font=FONT)
    id_label.grid(column=0, row=2, sticky=tk.E, padx=PADDING, pady=PADDING)
    id_entry = ttk.Entry(root, font=FONT)
    id_entry.grid(column=1, row=2, padx=PADDING, pady=PADDING)

    a_btn = ttk.Radiobutton(root, text="A")
    a_btn.grid(column=0, row=3, sticky=tk.W, padx=PADDING)
    b_btn = ttk.Radiobutton(root, text="B")
    b_btn.grid(column=0, row=4, sticky=tk.W, padx=PADDING)
    ab_btn = ttk.Radiobutton(root, text="AB")
    ab_btn.grid(column=0, row=5, sticky=tk.W, padx=PADDING)
    o_btn = ttk.Radiobutton(root, text="O")
    o_btn.grid(column=0, row=6, sticky=tk.W, padx=PADDING)

    rh_box = ttk.Checkbutton(root, text="Rh Positive")
    rh_box.grid(column=1, row=4, padx=PADDING, pady=PADDING)

    center_label = ttk.Label(root, text="Nearest Donation Center")
    center_label.grid(column=2, row=0, padx=PADDING, pady=PADDING)
    dropdown_box = ttk.Combobox(root)
    dropdown_box.grid(column=2, row=1, padx=PADDING, pady=PADDING)

    ok_btn = ttk.Button(root, text="Ok")
    ok_btn.grid(column=1, row=6, padx=PADDING, pady=PADDING)
    cancel_btn = ttk.Button(root, text="Cancel")
    cancel_btn.grid(column=2, row=6, padx=PADDING, pady=PADDING)

    root.mainloop()
    print("Finished")


if __name__ == "__main__":
    main_window()
