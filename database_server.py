import logging
from pymodm import connect
from flask import Flask, request, jsonify
from database_classes import Patient
from pymodm import errors as pymodm_errors


app = Flask(__name__)

db = []


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    """Adds new patient to database server

    This function implements the "/new_patient" route of the server.  It
    receives a POST request with the following JSON dictionary:

    {"name": str, "id": int, "blood_type": str}

    The "name" key should contain a string value with the name of the patient.
    The "id" key should contain an integer value with the medical record
    number of the patient.  The "blood_type" key should contain a string with
    the patient's blood type.

    The function then calls a function to validate that the input JSON has the
    correct keys and data types.  If there is a validation problem, an
    error message is returned as a response.  Next, the provided blood type is
    checked to ensure it is a valid entry.  If not, an error message is sent
    as a response.  When all the data checks out, a new patient is added to
    the database and a success message is returned as a response

    Returns
        str: Message about success or failure of request
        int: Status code

    """
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
    new_patient = Patient(mrn=in_data["id"],
                          name=in_data["name"],
                          blood_type=in_data["blood_type"])
    new_patient.save()
    return new_patient


def validate_blood_type(blood_type):
    if blood_type not in ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]:
        return "Provided blood type of {} is not valid".format(blood_type)
    else:
        return True


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results_patient_id(patient_id):
    """Returns patient test results from the database based on provided
    patient_id

    This function implements a GET request with the variable URL
    "get_results/<patient_id>" where the <patient_id> variable in the URL
    should contain the medical record number for a patient in the database.
    This function first validates that the provided mrn is in fact an
    integer.  Next, it attempts to get the patient from the database with
    that mrn.  If the mrn is not an integer, or if the given mrn does not
    exist in the database, an error message is returned as a response.
    Otherwise, the test results list of the found patient is returned as a
    JSON string.

    Args:
        patient_id (str): portion of variable URL containing the medical record
            number of the patient to be found

    Returns:
        str: Either an error message or a JSON list of test results
        int: Status code

    """
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
    try:
        patient = Patient.objects.raw({"_id": mrn}).first()
    except pymodm_errors.DoesNotExist:
        return False
    return patient


def add_test(patient, test_name, test_result):
    item = (test_name, test_result)
    patient.tests.append(item)
    patient.save()


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
    add_test(patient, in_data["test_name"], in_data["test_result"])
    return "Successfully added test", 200


def populate_database():
    x = Patient(1, "one", "O+")
    db.append(x)
    y = Patient(2, "two", "O-")
    db.append(y)


def initialize_server():
    logging.basicConfig(filename="server.log", filemode='w',
                        level=logging.DEBUG)
    logging.info("Started server")
    connect("mongodb+srv://fall24:fall24@bme547.ba348.mongodb.net/"
            "server_database?retryWrites=true&w=majority&appName=BME547")

if __name__ == "__main__":
    # populate_database()
    initialize_server()
    app.run()
