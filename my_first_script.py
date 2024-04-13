import formuls as fr
import json

with open('parallelepipeds.json', 'r') as json_file:
    data = json.load(json_file)

test_dict = list(data['figure_1'].values())
print(test_dict)