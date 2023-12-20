import json

with open('Data.json','r') as f:
  data = json.load(f)
print(data)
  
data['langage']='python'

new_json = json.dumps(data)
print(new_json)

with open('Data.json','w') as f:
  json.dump(data,f,indent=2)