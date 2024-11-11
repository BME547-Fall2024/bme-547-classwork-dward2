import base64
import requests

fn = "blue_devil.jpg"

# Input:
#    filename: string variable containing the path and name of the image file
#                on computer

with open(fn, "rb") as image_file:
    b64_bytes = base64.b64encode(image_file.read())
b64_string = str(b64_bytes, encoding='utf-8')

# Output:
#    b64_string: string variable containing the image bytes encoded as a base64
#                  string

out_json = {"image": b64_string, "net_id": "daw74", "id_no": 12}
server = "http://vcm-43716.vm.duke.edu"
r = requests.post(server + "/add_image", json=out_json)
print(r.status_code)
print(r.text)

# Get Image
# Make Get Request to Server
# Get r.text as base-64 string
# Convert base-64 string to a file, using a new filename of your choice
# Open file and make sure it has the watermark
