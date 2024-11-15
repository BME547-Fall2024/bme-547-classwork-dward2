from pymodm import MongoModel, fields


class Patient(MongoModel):
    mrn = fields.IntegerField(primary_key=True)
    name = fields.CharField()
    blood_type = fields.CharField()
    tests = fields.ListField()
