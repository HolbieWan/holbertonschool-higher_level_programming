#!/usr/bin/python3
"""CSV to json Module"""

import csv
import json


def convert_csv_to_json(filename):
    """Method to convert a csv file into json"""
    csv_list = []
    with open(filename, "r", encoding="utf-8", newline='') as csv_file:
        csv_dict = csv.DictReader(csv_file)
        for row in csv_dict:
            csv_list.append(row)

    with open("data.json", mode='w') as json_file:
        json_file.write('[\n')
        for i, item in enumerate(csv_list):
            json.dump(item, json_file)
            if i < len(csv_list) - 1:
                json_file.write(',\n')
        json_file.write('\n]')