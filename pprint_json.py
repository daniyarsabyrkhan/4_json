import json


def load_data(filepath):
    with open(filepath, "r") as jsonfile:
        jsonlist = json.load(jsonfile)
        return jsonlist


def pretty_print_json(data):
    print ("Теперь удобно читать: \n %s" % json.dumps(
        data, indent=4, sort_keys=True))


if __name__ == '__main__':
    filepath = input("Укажите путь до json файла: ")
    jsonlist = load_data(filepath)
    pretty_print_json(jsonlist)
