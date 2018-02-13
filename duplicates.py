import os
import sys
import collections


def get_files_locations_dict(path):
    files_locations_dict = collections.defaultdict(list)
    for root, _, filenames in os.walk(path):
        for file_name in filenames:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            files_locations_dict[(file_name, file_size)].append(file_path)
    return files_locations_dict


def get_duplicate_files(files_locations_dict):
    duplicate_dict = {}
    for (file_name, file_size), file_locations in files_locations_dict.items():
        if len(file_locations) > 1:
            duplicate_dict[(file_name, file_size)] = file_locations
    return duplicate_dict


def pretty_print_same_files(duplicate_dict):
    print("Same files: ")
    for (file_name, file_size), file_locations in duplicate_dict.items():
        print("File name: {}".format(file_name))
        print("File size: {} bytes".format(file_size))
        print("File paths:")
        for file_path in file_locations:
            print(file_path)
        print()


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Arguments error")
    else:
        if os.path.isdir(file_path):
            file_location_dict = get_files_locations_dict(file_path)
            duplicates = get_duplicate_files(file_location_dict)
            if duplicates:
                pretty_print_same_files(duplicates)
            else:
                print("There are no duplicates in the directory")
        else:
            print("Argument is not directory")