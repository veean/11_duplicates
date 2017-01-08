import os
import sys


def find_duplicates(path):
    size_and_path_table = {}
    for dirs, _, files in os.walk(path):
        for file in files:
            path_to_file = os.path.join(dirs, file)
            file_size = os.path.getsize(path_to_file)
            if file_size in size_and_path_table:
                size_and_path_table[file_size].append(path_to_file)
            else:
                size_and_path_table[file_size] = [path_to_file]
    return size_and_path_table


def has_duplicates(filename_entries):
    return len(filename_entries) > 1


def are_files_duplicates(path_to_analyze):
    files_table = find_duplicates(path_to_analyze)
    results = [x for x in files_table.values() if has_duplicates(x)]
    if results:
        for result in results:
            for result_part in result:
                print(result_part)
    else:
        print('None of duplicate files')


if __name__ == '__main__':

    try:
        if sys.argv[1]:
            start_path = str(sys.argv[1])
            if not os.path.exists(start_path):
                print("Invalid directory!")
            else:
                print('Duplicate files list :')
                are_files_duplicates(start_path)

    except IndexError as e:
        print("Choose directory to search ...")
