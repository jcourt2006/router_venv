import json

def load_data(filename):
    with open(filename, 'r') as infile:
        content = infile.read()
        db = json.loads(content)
    return db

def save_data(filename, dictionary):
    with open(filename, 'w') as outfile:
        content = json.dumps(dictionary, indent=2)
    return dictionary

if __name__ == "__main__":
    infile = "db.json"
    db = load_data(infile)
    for key in db:
        print(key)

