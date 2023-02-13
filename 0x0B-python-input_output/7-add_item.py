import sys


def save_to_json_file(my_obj, filename):
    import json
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    import json
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
