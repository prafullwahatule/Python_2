# Access the value of age from the given data
#Student_data = {"name":"Prafull","age":22,"marls":98}

import json
Student_data = {"name":"Prafull","age":22,"marls":98}
data = json.dumps(Student_data,indent=4,separators=(",","="))
print(data)