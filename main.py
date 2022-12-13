""" folder = input("joao@joao:~$ ")
print(f"joao@joao:~/{folder}$") """
from directory import Directory

"""
# Criando o diretório raiz
raiz = Directory("/")
home = Directory("home")
# Criando um sub diretório "home" no diretório "raiz"
raiz.make_sub_dir(home)
print(raiz)
# Criando um sub diretório "documents" no diretório "home"
documents = Directory("documents")
home.make_sub_dir(documents)
print(raiz)
# Criando um arquivo no diretório "raiz"
raiz.create_file("text.txt")
print(raiz)
# Movendo o arquivo para o sub diretório "documents"
raiz.move_file("text.txt", documents)
print(raiz)
"""
raiz = Directory("/")
print(raiz)
# Criando um sub diretório "home" dentro do diretório "raiz"
raiz.make_sub_dir("home")
# Pegando a instância do sub diretório "home" 
home = raiz.get_directory("home")
print(home)
# Criando um sub diretório "documents" no diretório home
home.make_sub_dir("documents")
# Pegando a instância do sub diretório "documents"
documents = home.get_directory("documents")
print(documents)
# Criando um arquivo no diretório "raiz"
raiz.create_file("Text.txt")
print(raiz)
# Movendo o arquivo para o diretório "documents"
raiz.move_file("Text.txt", documents)
print(documents._dir_files, documents._sub_dir)
print(raiz)
# Tupla com as opções disponíveis para o usuário
options = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "help", "exit", "test")
# Fazendo um while que termina quando o usuário escolha a opção "exit"
while True:
    # Criando um input para o usuário escolher as opções
    user_input = input("joao@joao:~$ ")
    command = user_input.split(" ")[0]
    # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
    while command not in options:
        print("Command not found. Type `help' to see command list")
        break
    # Opção "new"
        # Cria um arquivo
    if command == "new":
        file_name = user_input.split(" ")[1]
        raiz.create_file(file_name)
    # Opção "del"
        # Exlcui um arquivo
    if command == "del":
        remove_file_name = user_input.split(" ")[1]
        if file_name not in raiz._dir_files:
            print("File does not exist")
        else:
            del raiz._dir_files[remove_file_name]
    # Opção "ls"
        # Mostra todo o conteúdo dos diretórios
    if command == "ls":
        print("/")
        raiz.list_all()
    # Opção "mkdir"
        # Cria um novo diretório
    if command == "mkdir":
        user_option = user_input.split(" ")
        if len(user_option) == 3:
            new_dir_name = user_option[1]
            new_dir_name = Directory(new_dir_name)
            dir_name = user_option[2]
            dir = raiz.get_directory(dir_name)
            dir._sub_dir[new_dir_name._dir_name] = new_dir_name._sub_dir
            print(dir._sub_dir)
            print(new_dir_name)
        else:
            new_dir = user_option[1]
            # Criando um novo diretório, fora do diretório raiz (que é "/")
            new_dir = Directory(new_dir)
            # Colocando o novo diretório dentro do raiz
            raiz.make_sub_dir(new_dir._dir_name)
    # Opção "rmdir"
        # Remove o diretório selecionado
    if command == "rmdir":
        remove_dir_name = user_input.split(" ")[1]
        if remove_dir_name not in raiz._sub_dir:
            print("Dir does not exist")
        else:
            raiz.delete_sub_dir(remove_dir_name)
    # Opção "cp"
        # Faz uma cópia do arquivo para um novo diretório
    if command == "cp":
        file_name = user_input.split(" ")[1]
        dir_name = user_input.split(" ")[2]
        if file_name not in raiz._dir_files:
            print("File does not exist")
        elif dir_name not in raiz._sub_dir:
            print("Dir does not exist")
        else:
            dir = raiz.get_directory(dir_name)
            copy_file_value = raiz._dir_files.get(file_name)
            dir._dir_files[file_name] = copy_file_value
    # Opção "mv"
        # Move o arquivo para um novo diretório e exclui do anterior
    if  command == "mv":
        file_name = user_input.split(" ")[1]
        dir_name = user_input.split(" ")[2]
        if file_name not in raiz._dir_files:
            print("File does not exist") 
        elif dir_name not in raiz._sub_dir:
            print("Dir does not exist")        
        else:
            copy_file_value = raiz._dir_files.get(file_name)
            dir = raiz.get_directory(dir_name)
            dir._dir_files[file_name] = copy_file_value            
            del raiz._dir_files[file_name]
    # Opção "help"
        # Mostra os comandos disponíveis
    if command == "help":
        for option in options:
            print(" " , option)
    # Opção "test"
    if command == "test":
        pass
    # Opção "exit"
        # Fecha o programa
    if command == "exit":
        break
        exit()