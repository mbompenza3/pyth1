import json
# student1 = {
#     'first_name': 'Greg',
#     'last_name': 'Dean',
#     'scores': [70, 80, 90],
#     'description': "Good job, Greg",
#     'certificate': True
# }
#
# student2 = {
#     'first_name': 'Wirt',
#     'last_name': 'Wood',
#     'scores': [80, 80.2, 80],
#     'description': "Nicely Done",
#     'certificate': True
# }
#
# data = [student1, student2]
# data_json = json.dumps(data, indent=4, sort_keys=True)
# # print(data_json)
# data_again = json.loads(data_json)
# print(data_again)
# print(type(data_again))
# print(sum(data_again[0]["scores"]))

# print(json.dumps(data, indent=4, sort_keys=True))
# with open("students.json", "w") as f:
#     json.dump(data, f, indent=4, sort_keys=True)

# with open("students.json", "r") as f:
#     data_again = json.load(f)
#     print(sum(data_again[1]["scores"]))

dd={}
data=[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
d_js=json.dumps(data)
for d1 in data:
    if d1["name"] not in dd:
        dd[d1["name"]]=0
        for d2 in data:
            if d1["name"] in d2["parents"]:
                dd[d1["name"]] +=1
    print(d1["parents"])
print(dd)
