import json
import os
import pprint


def input_way_to_filepath():
    way = input('Укажите путь к файлу:')
    if os.path.exists(way):
        return way


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as alco_shops:
            data = json.load(alco_shops)
            return data


def pretty_print_json(data):
    pprint.pprint(data)


if __name__ == '__main__':
    filepath = input_way_to_filepath()
    data = load_data(filepath)
    pretty_print_json(data)
