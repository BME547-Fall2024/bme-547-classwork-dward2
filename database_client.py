import requests

server = "http://127.0.0.1:5000"
# server = "http://vcm-43729.vm.duke.edu:5000"

out_json = {"id": 101,
            "name": "Ann Ables",
            "blood_type": "A+"}

r = requests.post(server + "/new_patient",
                  json=out_json)
print(r.status_code)
print(r.text)


out_json = {"id": 101,
            "test_name": "HDL",
            "test_result": 60}

r = requests.post(server + "/add_test",
                  json=out_json)
print(r.status_code)
print(r.text)

r = requests.get(server + "/get_results/101")
print(r.status_code)
print(r.text)
