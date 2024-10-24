from pymodm import connect, MongoModel, fields
import time

connect("mongodb+srv://fall24:fall24@bme547.ba348.mongodb.net/intro_class?retryWrites=true&w=majority&appName=BME547")

class Patient(MongoModel):
    id = fields.IntegerField(primary_key=True)
    name = fields.CharField()

def add_user(id, name):
    u = Patient(id=id, name=name)
    u.save()

add_user(101, "Bob")
# time.sleep(5)

# for item in Patient.objects.raw({}):
#     print(item.name)

# print("Here")

