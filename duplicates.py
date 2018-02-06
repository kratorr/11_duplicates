import os
import sys
import collections


def get_file_key_dict(path):
    file_key_dict = collections.defaultdict(list)
    for root, _, filenames in os.walk(path):
        for file_name in filenames:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            file_key_dict[(file_name, file_size)].append(file_path)
    return file_key_dict


def get_duplicate_files(filename_size_dict):
    duplicate_dict = filename_size_dict
    for file_key in list(filename_size_dict):
        if len(filename_size_dict[file_key]) <= 1:
            filename_size_dict.pop(file_key)
    return duplicate_dict


def pretty_print_same_files(duplicate_dict):
    if duplicate_dict:
        print("Same files: ")
        for file_key in duplicate_dict:
            print("File name: {}".format(file_key[0]))
            print("File size: {} bytes".format(file_key[1]))
            print("File paths:")
            for file_path in duplicate_dict[file_key]:
                print(file_path)
            print()
    else:
        print("There are no duplicates in the directory")


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        if os.path.isdir(file_path):
            file_key_dict = get_file_key_dict(file_path)
            duplicates = get_duplicate_files(file_key_dict)
            pretty_print_same_files(duplicates)
        else:
            print("Argument is not directory")
    except IndexError:
        print("Arguments error")
