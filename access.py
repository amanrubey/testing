import json
import pandas as pd
file_path = 'posts_data.json'
with open(file_path,'r') as file:
  data = json.load(file)

# title_of_first_person = data['posts'][0]['title']
# body_of_first_person = data['posts'][0]['body']

# print(body_of_first_person)
# data = [{
#   'aman': 2,
#   'ame': [1,2,3]
# }]
df = pd.DataFrame(data)
print(df)
