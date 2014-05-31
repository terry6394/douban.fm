#encoding:utf-8

import sys
import os


def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def import_file(full_path_to_module):
    #try:
        module_dir, module_file = os.path.split(full_path_to_module)
        module_name, module_ext = os.path.splitext(module_file)
        sys.path.append(module_dir)
        module_obj = __import__(module_name)
        module_obj.__file__ = full_path_to_module
        globals()[module_name] = module_obj
    #except Exception, e:
        #raise ImportError(e)

import_file(cur_file_dir() + "/../get_song_list.py")

print get_song_list.get_songlist()
