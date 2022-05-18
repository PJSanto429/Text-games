'''import pickle  #this is probably not going to be the way that stuff is done; json is better

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

# none of this works :()
import json  #this is a better way to read and write data for this game

def Merge(dict1, dict2):
    return(dict2.update(dict1))

data = {
    "players":[
        {
            "name": "peyton",
            "room": "kitchen",
            "score": 500,
            "access": "super-admin"
        }
    ]
}

'''choice = input('Would you like to save game? ')
if choice == 'yes':
    name = input('Enter a name for the new save slot: ')
    room = input('enter room for save slot: ')
    score = input('enter score for save slot: ')
    access = 'user'''

def write_json(new_data, filename='data2.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["players"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

test2 = {
    "players":[
        {
            "name": 'steve',
            "room": 'library',
            "score": 50,
            "access": 'user'
        }
    ]
}

write_json(test2)

#x = json.dumps(data)
#y = json.dumps(data2)

#with open('data2.json', 'w') as outfile:
#    outfile.update(y)
#    outfile.write(x)

#with open ('data2.json', 'r') as infile:
#    data = json.load(infile)

    #print(data['emp_details'][1]["emp_name"]) #this is how you print the second name in the first dicitonary

    #getting items from a list in a dicitonary
    # https://pythonexamples.org/python-list-of-dictionaries/

    #python dictionaries and how to use them(refresher)
    # https://www.w3schools.com/python/python_dictionaries.asp
    
    # reading and writing to a json file
    # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/