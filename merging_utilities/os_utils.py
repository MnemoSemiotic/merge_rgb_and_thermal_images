from os import getcwd, listdir, makedirs
from os.path import exists, isdir, join

def get_img_dir(rel_dir='/images/'):
    canon_dir = getcwd() + rel_dir
    return canon_dir

def get_img_sets(canon_dir=get_img_dir(), print_subdirectories=False):
    directories = [name for name in listdir(canon_dir) if isdir(join(canon_dir, name))]

    if print_subdirectories == True:
        print(f'\nsubdirectories: \n    {directories}')

    image_set_filenames = dict()

    for directory in directories:
        file_list = listdir(canon_dir+directory)
        file_list = [filename for filename in file_list if '.jpg' in filename]
        image_set_filenames[directory] = file_list

    return image_set_filenames


def verify_parallel_filenames(img_set):
    directories = img_set
    not_parallel = []
    parallel = []

    for dir1 in directories.keys():
        for dir2 in directories.keys():
            if dir1 == dir2:
                continue

            if directories[dir1] != directories[dir2]:
                if (dir1, dir2) not in not_parallel and (dir2, dir1) not in not_parallel:
                    print(f'\nWarning: {dir1} and {dir2} directories are NOT PARALLEL')
                    not_parallel.append((dir1, dir2))
            else:
                if (dir1, dir2) not in parallel and (dir2, dir1) not in parallel:
                    print(F'\nYAY!, {dir1} and {dir2} directories are PARALLEL!')
                    parallel.append((dir1, dir2))
    return parallel, not_parallel
