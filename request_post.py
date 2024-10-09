import requests

out_json = {
    "name": "David Ward",
    "net_id": "daw74"
}

r = requests.get("http://vcm-43716.vm.duke.edu:5000", json=out_json)
print(r.status_code)
print(r.text)
