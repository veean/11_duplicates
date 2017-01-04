import os
import hashlib


def find_duplicates(path):
    hash_table = {}
    for dirs, subdirs, files in os.walk(path):
        for file in files:
            path_to_file = os.path.join(dirs, file)
            file_hash = hashlib.md5(open(path_to_file, 'rb').read()).hexdigest()
            if file_hash in hash_table:
                hash_table[file_hash].append(path_to_file)
            else:
                hash_table[file_hash] = [path_to_file]
    return hash_table

def are_files_duplicates(path_to_analyze):
    files_table = find_duplicates(path_to_analyze)
    results = [x for x in files_table.values() if len(x) > 1]
    if results:
        for result in results:
            for result_part in result:
                print(result_part)
    else:
        print('None of duplicate files')


if __name__ == '__main__':
    # find_duplicates('.')
    are_files_duplicates('C:\\Users\\root\\Desktop\\123')
