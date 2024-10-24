from mongo_work import Patient
from pymodm import connect


connect("mongodb+srv://fall24:fall24@bme547.ba348.mongodb.net/intro_class?retryWrites=true&w=majority&appName=BME547")


def test_retrieve():
    answer = Patient.objects.raw({}).first()
    print(answer)
    print(answer.name)
    assert answer.name == "Bob"

# def add_patient():
#     u = Patient(name="Dave", id=5)
#     u.save()


test_retrieve()
# add_patient()

# for item in Patient.objects.raw({}):
#     print(item.name)
