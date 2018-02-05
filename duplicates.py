import os
import sys


def get_root_dirs_files(path):
    root_dirs_files = []
    for root, dirs, filename in os.walk(path):
        root_dirs_files.append([root,dirs,filename])
    return root_dirs_files


def get_all_file_list(root_dirs_files):
    all_file_list = []
    for dir_tuple in root_dirs_files:
        for file_name in dir_tuple[2]:
            all_file_list.append(os.path.join(dir_tuple[0], file_name))
    return all_file_list


def create_filename_size_dict(file_list):
    filename_size_dict = {}
    for file in file_list:
        if (os.path.basename(file), os.path.getsize(file)) not in filename_size_dict:
            filename_size_dict[(os.path.basename(file), os.path.getsize(file))] = [file]
        else:
            pass
            filename_size_dict[(os.path.basename(file), os.path.getsize(file))].append(file)
    return filename_size_dict


def delete_non_duplicate_files(filename_size_dict):
    duplicate_dict = filename_size_dict
    for file_key in list(filename_size_dict):
        if len(filename_size_dict[file_key]) <= 1:
            filename_size_dict.pop(file_key)
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


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        if os.path.isdir(file_path):
            root_dirs_files = get_root_dirs_files(file_path)
            file_list = get_all_file_list(root_dirs_files)
            duplicate_dict = delete_non_duplicate_files(create_filename_size_dict(file_list))
            pretty_print_same_files(duplicate_dict)

        else:
            print("Argument is not directory")
    except IndexError:
        print("Arguments error")
    except ValueError:
        print("The specified file format does not match")
