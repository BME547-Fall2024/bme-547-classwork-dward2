import pytest
from database_server import app

client = app.test_client()

# Should include the tests from the `test_Patient.py` file.


@pytest.mark.parametrize("in_data, expected", [
    ({"one": 1, "two": "s"}, True),
    ({"two": "s"}, "The key one was not found"),
    ({"one": "1", "two": "s"}, "The value for key one had the wrong data "
                               "type."),
    ({"one": 1, "two": 2}, "The value for key two had the wrong data type.")
])
def test_validate_input_data(in_data, expected):
    from database_server import validate_input_data
    expected_keys = ["one", "two"]
    expected_types = [int, str]
    answer = validate_input_data(in_data, expected_keys, expected_types)
    assert answer == expected


def test_add_patient_to_database():
    from database_server import add_patient_to_database, db
    db.clear()
    in_data = {"id": 123,
               "name": "David",
               "blood_type": "O+"}
    add_patient_to_database(in_data)
    assert len(db) == 1
    assert db[0].mrn == 123


@pytest.mark.parametrize("blood_type, expected", [
    ("O+", True),
    ("O#", "Provided blood type of O# is not valid")
])
def test_validate_blood_type(blood_type, expected):
    from database_server import validate_blood_type
    answer = validate_blood_type(blood_type)
    assert answer == expected


@pytest.mark.parametrize("mrn, expected", [
    (1, "One"),
    (2, "Two"),
    (3, False)
])
def test_get_patient_from_db(mrn, expected):
    from database_server import get_patient_from_db, db, Patient
    db.clear()
    db.append(Patient(1, "One", "O+"))
    db.append(Patient(2, "Two", "A-"))
    answer = get_patient_from_db(mrn)
    if expected is False:
        assert answer == expected
    else:
        assert answer.name == expected


def test_post_new_patient():
    from database_server import db
    db.clear()
    in_json = {"id": 1, "name": "David", "blood_type": "O+"}
    response = client.post("/new_patient", json=in_json)
    assert response.status_code == 200
    assert response.text == "Successfully added"
    assert len(db) == 1
    assert db[0].name == "David"


def test_post_new_patient_error():
    from database_server import db
    db.clear()
    in_json = {"ixd": 1, "name": "David", "blood_type": "O+"}
    response = client.post("/new_patient", json=in_json)
    assert response.status_code == 400
    assert len(db) == 0


@pytest.mark.parametrize("mrn, expected", [
    (1, "One"),
    (2, "Two"),
    (3, False)
])
def test_get_get_results_patient_id(mrn, expected):
    from database_server import get_patient_from_db, db, Patient
    db.clear()
    db.append(Patient(1, "One", "O+"))
    db.append(Patient(2, "Two", "A-"))
    answer = client.get("/get_results/{}".format(mrn))
    if expected is False:
        assert answer.status_code == 400
    else:
        assert answer.status_code == 200
        assert answer.get_json() == []
