import os
import sys


def find_possible_duplicates(path):
    size_and_path_table = {}
    for dirs, _, files in os.walk(path):
        for file in files:
            path_to_file = os.path.join(dirs, file)
            file_size = os.path.getsize(path_to_file)
            if size_and_path_table.get(file_size, False):
                size_and_path_table[file_size].append(path_to_file)
            else:
                size_and_path_table[file_size] = [path_to_file]
    return size_and_path_table


def has_duplicates(filename_entries):
    return len(filename_entries) > 1


def get_files_duplicates(path_to_analyze):
    files_table = find_possible_duplicates(path_to_analyze)
    return [x for x in files_table.values() if has_duplicates(x)]


def print_files_duplicates(list_of_duplicates):
    print('A list of duplicate files : ')
    for duplicate in list_of_duplicates:
        for duplicate_entry in duplicate:
            print(duplicate_entry)


if __name__ == '__main__':

    try:
        if sys.argv[1]:
            start_path = str(sys.argv[1])
            if not os.path.exists(start_path):
                print("Invalid directory!")
            else:
                print_files_duplicates(get_files_duplicates(start_path))
    except IndexError as e:
        print("Choose directory to search ...")
