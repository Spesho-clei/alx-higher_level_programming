#!/usr/bin/python3
"""Save argument to a file."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

def add_items_to_list_and_save():
    try:
        # Load existing data from add_item.json if it exists
        try:
            existing_list = load_from_json_file('add_item.json')
        except FileNotFoundError:
            existing_list = []

        # Add command-line arguments to the list
        new_items = sys.argv[1:]
        updated_list = existing_list + new_items

        # Save the updated list to add_item.json
        save_to_json_file(updated_list, 'add_item.json')
        print('Added items: {}'.format(new_items))


    except Exception as e:
        print('Error: {}'.format(e))

if __name__ == "__main__":
    add_items_to_list_and_save()
