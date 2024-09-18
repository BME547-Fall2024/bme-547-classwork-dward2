"""
   patient = {"id": <id_num_as_int>,
              "test_name": <str>,
              "test_value": <int or float>}

Patient id: 1553
   Test Type:  HDL
   Test Value: 65
Patient id: 2344
   Test Type: HDL
   Test Value: 45
Patient id: 4427
etc.

"""


def make_new_patient(line):
    mrn, test_name, test_value = line.split(",")
    new_patient_dictionary = {"id": int(mrn),
                              "test_name": test_name,
                              "test_value": float(test_value)}
    return new_patient_dictionary


def output_db(db):
    for patient in db:
        print("Patient id: {}".format(patient["id"]))
        print("   Test Type: {}".format(patient["test_name"]))
        print("   Test Value: {}".format(patient["test_value"]))


def load_data():
    in_file = open("blood_test_data.txt", "r")
    db = []
    for line in in_file:
        new_patient = line.strip("\n")
        new_patient_dict = make_new_patient(new_patient)
        db.append(new_patient_dict)
    in_file.close()
    return db
    # with open("blood_test_data.txt", "r") as in_file:
    #     for line in in_file:
    #         new_patient = line.strip("\n")
    #         print(new_patient)


def main():
    db = load_data()
    output_db(db)


if __name__ == "__main__":
    main()
