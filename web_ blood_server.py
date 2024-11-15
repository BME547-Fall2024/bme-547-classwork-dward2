from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
patient_name = None
blood_letter = None
rh_factor = None

@app.route("/status", methods=["GET"])
def status():
    return render_template("status.html")

@app.route("/new_patient", methods=["GET", "POST"])
def new_patient():
    # global patient_name, blood_letter, rh_factor
    if request.method == "POST":
        patient_name = request.form["patient_name"]
        patient_mrn = request.form["mrn"]
        blood_letter = request.form["letter_choice"]
        rh_factor = request.form.get("rh_factor")
        if rh_factor is None:
            rh_factor = "-"
        center_choice = request.form["center_choice"]
        print(patient_name, blood_letter, rh_factor)
        out_dict = {"n": patient_name,
                    "mrn": patient_mrn,
                    "bl": blood_letter,
                    "rh": rh_factor,
                    "c": center_choice}
        out_data = json.dumps(out_dict)
        return redirect(url_for("results_handler", data=out_data))
    return render_template("blood_donor_web.html")


@app.route("/results/<data>", methods=["GET"])
def results_handler(data):
    in_data = json.loads(data)
    return render_template("input_result.html",
                           data=in_data)



if __name__ == "__main__":
    app.run()
