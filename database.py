"""
   patient = {"id": <id_num_as_int>,
              "tests": [(test_name, test_value),
                        (test_name1, test_value1), ...]}

Patient id: 1553
   Test Type:  HDL
   Test Value: 65
Patient id: 2344
   Test Type: HDL
   Test Value: 45
Patient id: 4427
etc.

"""

db = []


def make_new_patient(mrn, test_name, test_value):
    test_data = (test_name, test_value)
    new_patient_dictionary = {"id": mrn,
                              "tests": [test_data]}
    return new_patient_dictionary


def get_patient_from_db(mrn):
    # Search the database.
    for patient in db:
        # If the patient exists, return that patient.
        if patient["id"] == mrn:
            return patient
    return False
    # If not, return False


def output_db():
    for patient in db:
        print("Patient id: {}".format(patient["id"]))
        # print("Debug: {}".format(patient["tests"]))
        for test_info in patient["tests"]:
            print("   Test Type: {}".format(test_info[0]))
            print("   Test Value: {}".format(test_info[1]))


def add_test_to_patient(patient, test_name, test_value):
    test_data = (test_name, test_value)
    patient["tests"].append(test_data)


def load_data():
    in_file = open("blood_test_data.txt", "r")
    for line in in_file:
        mrn, test_name, test_value = line.strip("\n").split(",")
        mrn = int(mrn)
        test_value = float(test_value)
        existing_patient = get_patient_from_db(mrn)
        if existing_patient is False:
            new_patient_dict = make_new_patient(mrn, test_name, test_value)
            db.append(new_patient_dict)
        else:
            add_test_to_patient(existing_patient, test_name, test_value)
    in_file.close()

    # with open("blood_test_data.txt", "r") as in_file:
    #     for line in in_file:
    #         new_patient = line.strip("\n")
    #         print(new_patient)


def main():
    load_data()
    output_db()


if __name__ == "__main__":
    main()
