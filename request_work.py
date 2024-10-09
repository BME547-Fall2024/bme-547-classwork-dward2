import requests

url = "https://api.github.com//repos/dward2/BME547/branches"

r = requests.get(url)

# print(r)
# print(type(r))
# print(r.status_code)
# print(r.text)

print(type(r.text))
print(type(r.json()))

text_answer = r.text
answer = r.json()
print(answer[0]["name"])


branches = r.json()
# print("Branches contains: {}".format(branches))
for branch in branches:
    print(branch["name"])
