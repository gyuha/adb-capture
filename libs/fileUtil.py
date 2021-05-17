
import os


def current_dir_path():
    return os.getcwd()


def dir(path):
    return os.path.isdir(path) and [".."] + os.listdir(path) or ''


def dir_inner(cur_path, dir):
    moved = "%s/%s" % (cur_path, dir)

    if os.path.isdir(moved):
        return moved
    else:
        return cur_path


def removePathFiles(files):
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def dir_outer(path):
    dir_path_splits = path.split('/')[:-1]
    return "/".join(dir_path_splits)


def create_directory(cur_path, new_dir):
    new_dir = cur_path + '/' + new_dir

    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    else:
        new_dir = 0
    return new_dir


def rename(src, dis):
    if not os.path.exists(dis):
        os.rename(src, dis)
        return dis
    else:
        return 0


if __name__ == "__main__":
    """ test """

    current_path = current_dir_path()
    test_dir = 'test_dir'

    is_created_dir = create_directory(current_path, test_dir)

    print("current path : ", current_path)
    print("테스트 디렉토리 생성여부 : ", is_created_dir)

    dir_list = dir(current_path)
    print("correct directory list : ", dir_list)
    dir_list = dir(current_path+'12')
    print("in-correct directory list : ", dir_list)

    inner = dir_inner(current_path, test_dir)
    print("inner exists directory : ", inner)
    inner = dir_inner(current_path, '123')
    print("inner No exists directory : ", inner)

    outer1 = dir_outer(current_path)
    outer2 = dir_outer(inner)

    print("ouuter directory1 : ", outer1)
    print("ouuter directory2 : ", outer2)
