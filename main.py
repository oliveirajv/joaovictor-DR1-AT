""" folder = input("joao@joao:~$ ")
print(f"joao@joao:~/{folder}$") """

import random

from directory import Directory, ext4

options = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "help", "exit", "test")
# Fazendo um while para o programa rodar até que o usuário escolha a opção "exit"
while True:
    # Criando um input para o usuário escolher as opções
    user_command = input("joao@joao:~$ ")
    # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
    while user_command.split(" ")[0] not in options:
        print("Command not found. Type `help' to see command list")
        break
    # Opção "new"
        # Cria um arquivo
    if user_command.split(" ")[0] == "new":
        file_name = user_command.split(" ")[1]
        file_size = random.randrange(1, 8096)
        ext4._dir_files[file_name] = file_size
    # Opção "del"
        # Exlcui um arquivo
    if user_command.split(" ")[0] == "del":
        remove_file_name = user_command.split(" ")[1]
        if file_name not in ext4._dir_files:
            print("File does not exist")
        else:
            del ext4._dir_files[remove_file_name]
    # Opção "ls"
        # Mostra todo o conteúdo dos diretórios
    if user_command.split(" ")[0] == "ls":
        print("/")
        ext4.list_all()
    # Opção "mkdir"
        # Cria um novo diretório
    if user_command.split(" ")[0] == "mkdir":
        user_option = user_command.split(" ")
        if len(user_option) == 3:
            new_dir_name = user_option[1]
            new_dir_name = Directory(new_dir_name)
            dir_name = user_option[2]
            dir = ext4.get_directory(dir_name)
            dir._sub_dir[new_dir_name._dir_name] = new_dir_name._sub_dir
            print(dir._sub_dir)
            print(new_dir_name)
        else:
            new_dir = user_option[1]
            # Criando um novo diretório, fora do diretório raiz (que é "/")
            new_dir = Directory(new_dir)
            # Colocando o novo diretório dentro do raiz
            ext4.make_sub_dir(new_dir)
    # Opção "rmdir"
        # Remove o diretório selecionado
    if user_command.split(" ")[0] == "rmdir":
        remove_dir_name = user_command.split(" ")[1]
        if remove_dir_name not in ext4._sub_dir:
            print("Dir does not exist")
        else:
            del ext4._sub_dir[remove_dir_name]
    # Opção "cp"
        # Faz uma cópia do arquivo para um novo diretório
    if user_command.split(" ")[0] == "cp":
        file_name = user_command.split(" ")[1]
        dir_name = user_command.split(" ")[2]
        if file_name not in ext4._dir_files:
            print("File does not exist")
        elif dir_name not in ext4._sub_dir:
            print("Dir does not exist")
        else:
            dir = ext4.get_directory(dir_name)
            copy_file_value = ext4._dir_files.get(file_name)
            dir._dir_files[file_name] = copy_file_value
    # Opção "mv"
        # Move o arquivo para um novo diretório e exclui do anterior
    if  user_command.split(" ")[0] == "mv":
        file_name = user_command.split(" ")[1]
        dir_name = user_command.split(" ")[2]
        if file_name not in ext4._dir_files:
            print("File does not exist") 
        elif dir_name not in ext4._sub_dir:
            print("Dir does not exist")        
        else:
            copy_file_value = ext4._dir_files.get(file_name)
            dir = ext4.get_directory(dir_name)
            dir._dir_files[file_name] = copy_file_value            
            del ext4._dir_files[file_name]
    # Opção "help"
        # Mostra os comandos disponíveis
    if user_command.split(" ")[0] == "help":
        for option in options:
            print(" " + option)
    # Opção "test"
    if user_command.split(" ")[0] == "test":
        pass
    # Opção "exit"
        # Fecha o programa
    if user_command.split(" ")[0] == "exit":
        break
        exit()
