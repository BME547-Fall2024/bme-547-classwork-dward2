def test_make_new_patient():
    from database_class import make_new_patient
    mrn = 100
    test_name = "HDL"
    test_value = 55
    patient_name = "Ann Ables"
    answer = make_new_patient(mrn, test_name, test_value,
                              patient_name)
                              
    assert answer.mrn == mrn
    assert answer.name == patient_name
    
    
def test_get_patient_from_db():
    from database_class import get_patient_from_db, db, \
            make_new_patient, Patient
    # Arrange
    new_patient = make_new_patient(100, "HDL", 55, "Ann Ables")
    db.append(new_patient)
    new_patient2 = make_new_patient(101, "LDL", 66, "Bob Boyles")
    db.append(new_patient2)
    # Act
    answer = get_patient_from_db(101)
    # Assert
    expected = Patient(101, "Bob Boyles")
    expected.add_test("LDL", 66)
    db.clear()
    assert answer == expected
