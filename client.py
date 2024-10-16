import requests

server = "http://127.0.0.1:5000"
# server = "http://bme547.duke.edu:5000"

out_json = {"name": "David Ward",
            "HDL_value": 45}
r = requests.post(server + "/hdl", json=out_json)
print(r.status_code)
print(r.text)
