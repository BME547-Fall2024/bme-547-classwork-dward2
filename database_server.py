from flask import Flask, request, jsonify

app = Flask(__name__)


class Patient:

    def __init__(self, mrn, name, blood_type):
        self.mrn = mrn
        self.tests = []
        self.name = name
        self.blood_type = blood_type

    def __repr__(self):
        return "Patient: {}, {}".format(self.name,
                                        self.blood_type)

    def __eq__(self, other):
        if self.mrn == other.mrn and self.name == other.name:
            return True
        else:
            return False

    def print_data(self):
        print(self.mrn)
        print(self.name)
        print(self.tests)

    def add_test(self, test_name, test_value):
        test_data = (test_name, test_value)
        self.tests.append(test_data)


db = []


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Get the data sent with the request
    in_data = request.get_json()
    # Validate the data received
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    input_check = validate_input_data(in_data, expected_keys,
                                      expected_types)
    if input_check is not True:
        return input_check, 400
    blood_type_check = validate_blood_type(in_data["blood_type"])
    if blood_type_check is not True:
        return blood_type_check, 400
    # Implement the route
    add_patient_to_database(in_data)
    # Return a response
    return "Successfully added", 200


def validate_input_data(in_data, expected_keys, expected_types):
    for expected_key, expected_type in zip(expected_keys, expected_types):
        if expected_key not in in_data:
            return ("The key {} was not found"
                    .format(expected_key))
        if type(in_data[expected_key]) is not expected_type:
            return ("The value for key {} had the wrong data type."
                    .format(expected_key))
    return True


def add_patient_to_database(in_data):
    new_patient = Patient(in_data["id"], in_data["name"],
                          in_data["blood_type"])
    db.append(new_patient)
    print(db)


def validate_blood_type(blood_type):
    if blood_type not in ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]:
        return "Provided blood type of {} is not valid".format(blood_type)
    else:
        return True


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results_patient_id(patient_id):
    mrn = validate_patient_id_string(patient_id)
    if type(mrn) is not int:
        return mrn, 400
    patient = get_patient_from_db(mrn)
    if patient is False:
        return ("Patient id of {} does not exist in the database"
                .format(patient_id), 400)
    return jsonify(patient.tests), 200


def validate_patient_id_string(patient_id):
    try:
        mrn = int(patient_id)
    except ValueError:
        return "{} is not a valid patient_id".format(patient_id)
    return mrn


def get_patient_from_db(mrn):
    for patient in db:
        if patient.mrn == mrn:
            return patient
    return False


@app.route("/add_test", methods=["POST"])
def post_add_test():
    in_data = request.get_json()
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    input_check = validate_input_data(in_data, expected_keys, expected_types)
    if input_check is not True:
        return input_check, 400
    patient = get_patient_from_db(in_data["id"])
    if patient is False:
        return ("Patient id of {} not found in database".format(in_data["id"]),
                400)
    patient.add_test(in_data["test_name"], in_data["test_result"])
    return "Successfully added test", 200


if __name__ == "__main__":
    app.run()
