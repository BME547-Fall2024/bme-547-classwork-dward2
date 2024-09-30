class Patient:

    def __init__(self, mrn, name=None):
        self.mrn = mrn
        self.tests = []
        if name is None:
            self.name = "John Doe"
        else:
            self.name = name

    def __repr__(self):
        return "Patient: {}".format(self.name)

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
        test = []


db = []


def make_new_patient(mrn, test_name, test_value, patient_name):
    new_patient = Patient(mrn, patient_name)
    new_patient.add_test(test_name, test_value)
    return new_patient


def get_patient_from_db(mrn):
    # Search the database.
    for patient in db:
        # If the patient exists, return that patient.
        if patient.mrn == mrn:
            return patient
    return False
    # If not, return False


def load_data():
    in_file = open("blood_test_data.txt", "r")
    for line in in_file:
        data = line.strip("\n").split(",")
        mrn = int(data[0])
        test_name = data[1]
        test_value = float(data[2])
        if len(data) == 4:
            patient_name = data[3]
        else:
            patient_name = None
        existing_patient = get_patient_from_db(mrn)
        if existing_patient is False:
            new_patient_dict = make_new_patient(mrn, test_name, test_value,
                                                patient_name)
            db.append(new_patient_dict)
        else:
            existing_patient.add_test(test_name, test_value)
    in_file.close()


def main():
    x = Patient(101, "Dave")
    x.add_test("HDL", 100)
    print(x.tests)
    # load_data()
    # print(db)
    # for patient in db:
    #     patient.print_data()


if __name__ == "__main__":
    main()
