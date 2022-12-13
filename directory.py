from random import randrange

#from colored import fg, attr

class Directory:
    def __init__(self, _dir_name):
        self._dir_name = _dir_name
        # Conteúdo do diretório
        self._dir_files = {}
        self._sub_dir = {}
        self._parent = None
    # Pega diretório
    def get_directory(self, _dir_name):
        dir = self._sub_dir[_dir_name]
        return dir
    # Cria arquivo
    def create_file(self, _file_name):
        _file_size = randrange(1, 8096)
        self._dir_files[_file_name] = _file_size
    # Deleta arquivo
    def delete_file(self, _file_name, _dir_name):
        pass    
    # Lista conteúdo do diretório
    def list_all(self):
        #color = fg("slate_blue_1")
        #reset = attr("reset")
        for items in self._dir_files:
            print(" " , items , self._dir_files[items])
        for items in self._sub_dir:
            #print(color , items , self._sub_dir[items] , reset)
            print(items, self._sub_dir[items])
    # Cria sub diretório
    def make_sub_dir(self, _sub_dir):
        dir = Directory(_sub_dir)
        self._sub_dir[dir._dir_name] = dir
        # self._sub_dir[_sub_dir._dir_name] = _sub_dir._dir_files, _sub_dir._sub_dir
    # Deleta sub diretório
    def delete_sub_dir(self, _dir_name):
        del self._sub_dir[_dir_name]    
    # Copia arquivo
    def copy_file(self, _file_name, _dir_name):
        pass
    # Move arquivo
    def move_file(self, _file_name, _dir_name):
        file_size = self._dir_files.get(_file_name)
        _dir_name._dir_files[_file_name] = file_size 
        del self._dir_files[_file_name]   
    # Mostrando a classe Directory formatado
    def __str__(self):
        return str(self._dir_name) + str(self._dir_files) + str(self._sub_dir)
