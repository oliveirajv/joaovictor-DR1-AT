from colored import fg, attr

class Directory:
    def __init__(self, _dir_name):
        self._dir_name = _dir_name
        # Conteúdo do diretório
        self._dir_files = {}
        self._sub_dir = {}
    # Função que cria um sub diretório
    def make_sub_dir(self, _sub_dir):
        self._sub_dir[_sub_dir._dir_name] = _sub_dir
    # Função que lista o conteúdo do diretório
    def list_all(self):
        color = fg("slate_blue_1")
        reset = attr("reset")
        for items in self._dir_files:
            print(" " + items , self._dir_files[items])
        for items in self._sub_dir:
            print(" " + color , items , self._sub_dir[items] , reset)

    def get_directory(self, _dir_name):
        dir = self._sub_dir[_dir_name]
        return dir

    def delete_file(self, _file_name, _dir_name):
        pass

    def delete_directory(self, _dir_name):
        pass

    def copy_file(self, _file_name, _dir_name):
        pass

    def move_file(self, _file_name, _dir_name):
        pass

    def __str__(self):
        return self._dir_name + str(self._dir_files) + str(self._sub_dir)
ext4 = Directory("/")