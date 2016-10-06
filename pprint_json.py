import json
import os
import pprint


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as alco_shops:
            return json.load(alco_shops)


def pretty_print_json(data):
    num_data = int(input('введитеномер магазина='))
    if 0 < num_data < 813:
        pprint.pprint(data[num_data-1])
    else:
        print('Номер магазина не найден')


if __name__ == '__main__':
    data = load_data('alco_shops.json')
    pretty_print_json(data)
