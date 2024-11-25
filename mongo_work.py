from pymodm import connect, MongoModel, fields
import time
from database_definitions import Patient, Doctors
import os

mongo_pswd = os.environ.get('MONGODB')
print(mongo_pswd)

connect("mongodb+srv://fall24:{}@bme547.ba348.mongodb.net/intro_class?retryWrites=true&w=majority&appName=BME547".format(mongo_pswd))



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

