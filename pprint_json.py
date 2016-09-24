import json


def load_data(filepath):
    with open (filepath, "r") as jsondata:
    	jsondatas = json.load(jsondata)
    	return jsondatas


def pretty_print_json(data):
    print (json.dumps(data, indent = 4, sort_keys = True))


if __name__ == '__main__':
    filepath = input()
    jsonfile = load_data(filepath)
    pretty_print_json(jsonfile)