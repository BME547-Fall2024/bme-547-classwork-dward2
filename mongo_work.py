from pymodm import connect, MongoModel, fields
import time
from database_definitions import Patient, Doctors

connect("mongodb+srv://fall24:fall24@bme547.ba348.mongodb.net/intro_class?retryWrites=true&w=majority&appName=BME547")



def add_user(id, name):
    u = Patient(id=id, name=name)
    u.save()

if __name__ == "__main__":
    add_user(101, "Bob")
    d = Doctors(name="Name", hospital="hospital")
    d.save()
# time.sleep(5)

# for item in Patient.objects.raw({}):
#     print(item.name)

# print("Here")

