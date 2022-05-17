'''import pickle

stuff = {
    'name': 'steve',
    'score': '100',
    'room': 'basement'
}

#pickle_out = open('saveFile.txt', 'wb')
#pickle.dump(stuff, pickle_out)
#pickle_out.close()

pickle_in = open('saveFile.txt', 'rb')
example_dict = pickle.load(pickle_in)

print(f"name: {example_dict['name']}")
print(f"score: {example_dict['score']}")
print(f"room: {example_dict['room']}")'''

#test.py, data.json, and saveFile.txt are all for testing a save state feature.

import json
f = open('data.json')
data = json.load(f)

for i in data['emp_details']:
    print(i)

f.close()