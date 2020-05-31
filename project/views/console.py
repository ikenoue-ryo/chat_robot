import os
import string

#/Users/ryoikenoue/Desktop/projects/project/templates を返す
def find_path():
    dir_path = os.path.dirname(os.path.dirname(__file__))
    template = os.path.join(dir_path, 'templates')
    return template


#pathの作成と中身の読み込み
def get_file_path(file_name):
    dir_path = os.path.join(find_path(), file_name)

    with open(dir_path, 'r', encoding='utf-8') as file_path:
        contents = file_path.read()
        return string.Template(contents)