
import json
data = "today is a good day"
with open('you.txt', 'w') as file:
  a = json.dump(data,file)
print(data)