def test_make_new_patient():
    from database import make_new_patient
    mrn = 100
    test_name = "HDL"
    test_value = 55
    answer = make_new_patient(mrn, test_name, test_value)
    expected = {"id": mrn, "tests": [(test_name, test_value)]}
    assert answer == expected


def test_get_patient_from_db():
    from database import get_patient_from_db, db, \
            make_new_patient
    # Arrange
    new_patient = make_new_patient(100, "HDL", 55)
    db.append(new_patient)
    new_patient2 = make_new_patient(101, "LDL", 66)
    db.append(new_patient2)
    # Act
    answer = get_patient_from_db(101)
    # Assert
    expected = {"id": 101, "tests": [("LDL", 66)]}
    db.clear()
    assert answer == expected


def test_empty_db():
    from database import db
    assert len(db) == 0
