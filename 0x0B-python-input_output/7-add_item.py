#!/usr/bin/python3
"""import module here """
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


try:
    items = load("add_item.json")
except FileNotFoundError:
    items = []

for item in sys.argv[1:]:
    items.append(item)

save(items, "add_item.json")
