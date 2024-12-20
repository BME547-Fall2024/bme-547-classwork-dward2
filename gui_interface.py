import tkinter as tk
from itertools import count
from tkinter import ttk, messagebox, filedialog
import requests
from PIL import Image, ImageTk

SERVER = "http://127.0.0.1:5000"

FONT = None  # ("arial", 24)
PADDING = 5


def post_patient_to_server(name, mrn, blood_type):
    out_json = {"name": name,
                "id": mrn,
                "blood_type": blood_type}
    r = requests.post(SERVER + "/new_patient", json=out_json)
    return r.text


def load_image(image_fn):
    pil_image = Image.open(image_fn)
    x, y = pil_image.size
    picture_size = 200
    alpha_x = picture_size / x
    alpha_y = picture_size / y
    alpha = min(alpha_x, alpha_y)
    new_x = round(x * alpha)
    new_y = round(y * alpha)
    pil_image = pil_image.resize((new_x, new_y))
    return pil_image


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

    def image_select_btn_cmd():
        # Get info from GUI
        image_fn = filedialog.askopenfilename()
        if image_fn == "":
            return
        # Call other function to do the work
        pil_image = load_image(image_fn)
        # Update the GUI
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

    def change_label_color():
        if center_label.cget("foreground") == "black":
            center_label.configure(foreground="red")
        else:
            center_label.configure(foreground="black")
        root.after(2000, change_label_color)
    

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

    center_label = tk.Label(root, text="Nearest Donation Center", foreground="black")
    center_label.grid(column=2, row=0, padx=PADDING, pady=PADDING)
    county = tk.StringVar()
    dropdown_box = ttk.Combobox(root, values=("Durham", "Orange", "Wake"),
                                textvariable=county, state=["readonly"])
    dropdown_box.grid(column=2, row=1, padx=PADDING, pady=PADDING)

    image_select_btn = ttk.Button(root, text="Select Image",
                                  command=image_select_btn_cmd)
    image_select_btn.grid(column=3, row=0)

    pil_image = load_image("blank_avatar.png")
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.grid(column=3, row=1, padx=PADDING, pady=PADDING,
                     rowspan=10)

    ok_btn = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_btn.grid(column=1, row=6, padx=PADDING, pady=PADDING)
    cancel_btn = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_btn.grid(column=2, row=6, padx=PADDING, pady=PADDING)

    status_label = ttk.Label(root, text="")
    status_label.grid(column=0, row=7, padx=PADDING, pady=PADDING)

    root.after(2000, change_label_color)

    root.mainloop()
    print("Finished")


if __name__ == "__main__":
    main_window()
