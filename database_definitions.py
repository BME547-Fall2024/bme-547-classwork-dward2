from pymodm import MongoModel, fields

class Patient(MongoModel):
    id = fields.IntegerField(primary_key=True)
    name = fields.CharField()

class Doctors(MongoModel):
    name = fields.CharField()
    hospital = fields.CharField()