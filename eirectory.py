import random

from colored import fg, attr

class Directory:
    def __init__(self, _dir_name):
        self._dir_name = _dir_name
        # Conteúdo do diretório
        self._dir_files = {}
        self._sub_dir = {}
        self._parent = None
    def create_file(self, _file_name):
        _file_size = random.randrange(1, 8096)
        self._dir_files[_file_name] = _file_size
    def delete_file(self, _file_name, _dir_name):
        pass
    def get_directory(self, _dir_name):
        dir = self._sub_dir[_dir_name]
        return dir
    # Função que cria um sub diretório
    def make_sub_dir(self, _sub_dir):
        self._sub_dir[_sub_dir._dir_name] = _sub_dir
    # Função que lista o conteúdo do diretório
    def list_all(self):
        color = fg("slate_blue_1")
        reset = attr("reset")
        for items in self._dir_files:
            print(" " , items , self._dir_files[items])
        for items in self._sub_dir:
            print(" " + color , items , self._sub_dir[items] , reset)
    def delete_directory(self, _dir_name):
        del self._sub_dir[_dir_name]

    def copy_file(self, _file_name, _dir_name):
        pass

    def move_file(self, _file_name, _dir_name):
        pass

    def __str__(self):
        return self._dir_name + str(self._dir_files) + str(self._sub_dir)
ext4 = Directory("/")
