""" folder = input("joao@joao:~$ ")
print(f"joao@joao:~/{folder}$") """

import random

from directory import Directory, ext4

options = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "help", "exit")
# Fazendo um while para o programa rodar até que o usuário escolha a opção "exit"
while True:
    # Criando um input para o usuário escolher as opções
    user_option = input("joao@joao:~$ ")
    # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
    while user_option.split(" ")[0] not in options:
        print("Command not found. Type `help' to see command list")
        break
    # Opção "new"
    if user_option.split(" ")[0] == "new":
        file_name = user_option.split(' ')[1]
        file_size = random.randrange(1, 8096)
        ext4._dir_files[file_name] = file_size
        print(file_name + " created")
    # Opção "ls"
    if user_option.split(" ")[0] == "ls":
        ext4.list_all_()
    # Opção "mkdir"
    if user_option.split(" ")[0] == "mkdir":
        new_dir = user_option.split(' ')[1]
        # Criando um novo diretório, fora do diretório raiz (que é "/").
        new_dir = Directory(new_dir)
        # Colocando o novo diretório dentro do raiz
        ext4.make_sub_dir(new_dir)
        print("dir " + new_dir._dir_name + " created")
    # Mostrando as opções existentes quando o usuário escolhe a opção "help"
    if user_option.split(" ")[0] == "help":
        for option in options:
            print(" " + option)
    # Parando o while e fechando o programa quando o usuário escolhe a opção "exit" 
    if user_option.split(" ")[0] == "exit":
        break
        exit()
