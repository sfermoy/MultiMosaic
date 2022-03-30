import json, os
data = {}
i=0
path = "concordances2/"
for filename in os.listdir(path):
	s=open(path+filename, 'r').read()
	data[filename] = s

f= open("concordances2.json","w+")
json_data = json.dumps(data)
f.write(json_data)
f.close()