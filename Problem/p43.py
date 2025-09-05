# Sort the following json keys and write them into a fiele.
# Student_data = {"name":"Prafull","age":22,"marls":98}
import json
Student_data = {"name":"Prafull","age":22,"marls":98}
f = open("demo.json","w")
data = json.dumps(Student_data,indent = 4, sor_keys = True)
f.write(data)