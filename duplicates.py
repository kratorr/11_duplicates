import os
import sys
import collections


def get_file_location_dict(path):
    file_location_dict = collections.defaultdict(list)
    for root, _, filenames in os.walk(path):
        for file_name in filenames:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            file_location_dict[(file_name, file_size)].append(file_path)
    return file_location_dict


def get_duplicate_files(file_location_dict):
    duplicate_dict = file_location_dict
    for file_name in list(duplicate_dict):
        file_locations = duplicate_dict[file_name]
        if len(file_locations) <= 1:
            duplicate_dict.pop(file_name)
    return duplicate_dict


def pretty_print_same_files(duplicate_dict):
    print("Same files: ")
    for file_key in duplicate_dict:
        print("File name: {}".format(file_key[0]))
        print("File size: {} bytes".format(file_key[1]))
        print("File paths:")
        for file_path in duplicate_dict[file_key]:
            print(file_path)
        print()


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
        if os.path.isdir(file_path):
            file_location_dict = get_file_location_dict(file_path)
            duplicates = get_duplicate_files(file_location_dict)
            if duplicates:
                pretty_print_same_files(duplicates)
            else:
                print("There are no duplicates in the directory")
        else:
            print("Argument is not directory")
    except IndexError:
        print("Arguments error")
