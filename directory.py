from colored import fg, attr

class Directory:
    def __init__(self, _dir_name):
        self._dir_name = _dir_name
        # Conteúdo do diretório
        self._dir_files = {}
        self._sub_dir = {}

    def make_sub_dir(self, _sub_dir):
        self._sub_dir[_sub_dir._dir_name] = _sub_dir

    def list_all_(self):
        color = fg('slate_blue_1')
        reset = attr('reset')
        for items in self._dir_files:
            print(" " + items)
        for items in self._sub_dir:
            print(" " + color + items + reset)

    def __str__(self):
        return self._dir_name + str(self._dir_files)

ext4 = Directory("/")