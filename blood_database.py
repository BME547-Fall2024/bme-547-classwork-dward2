# print("This is the blood_database module")
# print("Python calls this {}".format(__name__))


import blood_calculator

HDL = 55
classification = blood_calculator.hdl_analysis(HDL)
print("The patient with HDL of {} is {}".format(HDL,
                                                classification))
