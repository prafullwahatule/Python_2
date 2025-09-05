# Convert the following dictionary into json format
# Student_data = {"name":"Prafull","age":22,"marls":98}


import json
Student_data = {"name":"Prafull","age":22,"marls":98}
print(type(Student_data))
data = json.dumps(Student_data)
print(data)
print(type(data))