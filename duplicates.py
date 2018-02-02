import os
import sys


def get_dirs_files_list(path):
    dirs_files_list = []
    for current_dir, dirs, files in os.walk(path):
        dirs_files_list.append([current_dir, dirs, files])
    return dirs_files_list


def get_file_list(dirs_files_list):
    file_list = []
    for dir_tuple in  dirs_files_list:
        for file_name in dir_tuple[2]:
            file_list.append(dir_tuple[0] + "/" + file_name)  # append full path to file
    return file_list


def compare_2_files(file_path_1, file_path_2):
    if os.path.basename(file_path_1) == os.path.basename(file_path_2):
        if os.path.getsize(file_path_1) == os.path.getsize(file_path_2):
            return True
    else:
        return False


def get_same_files_dict(file_list):
    same_files_dict = {}
    for file_1 in file_list:
        for file_2 in file_list:
            if file_1 != file_2:
                if compare_2_files(file_1, file_2):
                    if os.path.basename(file_1) in same_files_dict:
                        if file_1 not in same_files_dict[os.path.basename(file_1)][1]:
                            same_files_dict[os.path.basename(file_1)][1].append(file_1)
                    else:
                        same_files_dict[os.path.basename(file_1)] = [[os.path.getsize(file_1)], [file_1]]
    return same_files_dict


def pretty_print_same_files(same_files_dict):
    print("Same files: ")
    for file_name in same_files_dict:
        print("File name: {}".format(file_name))
        print("File size: {} bytes".format(same_files_dict[file_name][0]))
        print("File paths:")
        for file_path in same_files_dict[file_name][1]:
            print(file_path)
        print()


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        if os.path.isdir(file_path):
            file_list = get_file_list(get_dirs_files_list(file_path))
            same_files_dict = get_same_files_dict(file_list)
            pretty_print_same_files(same_files_dict)
        else:
            print("Argument is not directory")
    except IndexError:
        print("Arguments error")
    except ValueError:
        print("The specified file format does not match")
