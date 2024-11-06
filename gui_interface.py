import tkinter as tk
from itertools import count
from tkinter import ttk, messagebox
import requests

SERVER = "http://127.0.0.1:5000"

FONT = None  # ("arial", 24)
PADDING = 5


def post_patient_to_server(name, mrn, blood_type):
    out_json = {"name": name,
                "id": mrn,
                "blood_type": blood_type}
    r = requests.post(SERVER + "/new_patient", json=out_json)
    return r.text


def main_window():

    def cancel_btn_cmd():
        root.destroy()

    def ok_btn_cmd():
        # Get data from the GUI
        name_val = name_result.get()
        id_no = id_result.get()
        try:
            mrn = int(id_no)
        except ValueError:
            choice = messagebox.askyesno("Confirmation",
                                         "Are you sure you want to do this?")
            if choice:
                print("I'll do it")
            messagebox.showerror("Bad Validation",
                                 "The id was not an integer.")
            return
        blood_type_val = blood_type.get()
        rh_factor = rh_value.get()
        county_choice = county.get()
        # Call other functions to do the work
        full_blood_type = "{}{}".format(blood_type_val, rh_factor)
        result = post_patient_to_server(name_val, mrn, full_blood_type)
        # Update GUI as needed
        status_label.configure(text=result)
        print("Name: {}".format(name_val))
        print("ID: {}".format(id_no))
        print("Blood type: {}{}".format(blood_type_val, rh_factor))
        print("County: {}".format(county_choice))

    root = tk.Tk()
    root.title("Blood Database")
    # root.geometry("800x800")

    title_label = ttk.Label(root, text="Blood Donor Database", font=FONT)
    title_label.grid(column=0, row=0, columnspan=2, sticky=tk.W,
                     padx=PADDING, pady=PADDING)

    name_label = ttk.Label(root, text="Name:", font=FONT)
    name_label.grid(column=0, row=1, sticky=tk.E, padx=PADDING, pady=PADDING)
    name_result = tk.StringVar()
    name_entry = ttk.Entry(root, font=FONT, textvariable=name_result)
    name_entry.grid(column=1, row=1, padx=PADDING, pady=PADDING)

    id_label = ttk.Label(root, text="Id:", font=FONT)
    id_label.grid(column=0, row=2, sticky=tk.E, padx=PADDING, pady=PADDING)
    id_result = tk.StringVar()
    id_entry = ttk.Entry(root, font=FONT, textvariable=id_result)
    id_entry.grid(column=1, row=2, padx=PADDING, pady=PADDING)

    blood_type = tk.StringVar()
    a_btn = ttk.Radiobutton(root, text="A", variable=blood_type, value="A")
    a_btn.grid(column=0, row=3, sticky=tk.W, padx=PADDING)
    b_btn = ttk.Radiobutton(root, text="B", variable=blood_type, value="B")
    b_btn.grid(column=0, row=4, sticky=tk.W, padx=PADDING)
    ab_btn = ttk.Radiobutton(root, text="AB", variable=blood_type, value="AB")
    ab_btn.grid(column=0, row=5, sticky=tk.W, padx=PADDING)
    o_btn = ttk.Radiobutton(root, text="O", variable=blood_type, value="O")
    o_btn.grid(column=0, row=6, sticky=tk.W, padx=PADDING)

    rh_value = tk.StringVar()
    rh_value.set("+")
    rh_box = ttk.Checkbutton(root, text="Rh Positive", variable=rh_value,
                             onvalue="+", offvalue="-")
    rh_box.grid(column=1, row=4, padx=PADDING, pady=PADDING)

    center_label = ttk.Label(root, text="Nearest Donation Center")
    center_label.grid(column=2, row=0, padx=PADDING, pady=PADDING)
    county = tk.StringVar()
    dropdown_box = ttk.Combobox(root, values=("Durham", "Orange", "Wake"),
                                textvariable=county, state=["readonly"])
    dropdown_box.grid(column=2, row=1, padx=PADDING, pady=PADDING)

    ok_btn = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_btn.grid(column=1, row=6, padx=PADDING, pady=PADDING)
    cancel_btn = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_btn.grid(column=2, row=6, padx=PADDING, pady=PADDING)

    status_label = ttk.Label(root, text="")
    status_label.grid(column=0, row=7, padx=PADDING, pady=PADDING)

    root.mainloop()
    print("Finished")


if __name__ == "__main__":
    main_window()
