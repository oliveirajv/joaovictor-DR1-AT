""" folder = input("joao@joao:~$ ")
print(f"joao@joao:~/{folder}$") """
from eirectory import Directory, ext4

def input_treat(user_input):
    # Obtendo o comando   
    command = user_input.split(" ")
    # Verificando se existe algum comando e caminho
    if len(command) == 1:
        return print("Command not found. Type `help' to see command list") 
    # Se tiver os dois  
    else:
        # Pegando o caminho
        path = command.pop()
        # Separando o caminho por "/"   
        path = path.split("/")
        # Se o tamanho da lista do caminho for 1
        if len(path) == 1:
            # Diretório raiz
            # Retornando o nome do arquivo
            file_name = path.pop()
            return file_name
        # Senão        
        else:
            # Pegar caminho

            # Pegando o nome do arquivo
            file_name = path.pop()
            return file_name

options = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "help", "exit", "test")

# Fazendo um while para o programa rodar até que o usuário escolha a opção "exit"
while True:    
    # Criando um input para o usuário escolher as opções
    user_input = input("joao@joao:~$ ")
    # Pegando o comando
    command = user_input.split(" ")[0]
    # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
    while command not in options:
        print("Command not found. Type `help' to see command list")
        break
    # Opção "new"
        # Cria um arquivo
    if command == "new":
        if True:
            dir_name.create_file(input_treat(user_input))
    # Opção "del"
        # Exlcui um arquivo
    if command == "del":
        if user_input[1] == "":
            print("Command not found. Type `help' to see command list")
        else:
            remove_file_name = user_input.split(" ")[1]
            if file_name not in ext4._dir_files:
                print("File does not exist")
            else:
                del ext4._dir_files[remove_file_name]
    # Opção "ls"
        # Mostra todo o conteúdo dos diretórios
    if command == "ls":
        print("/")
        ext4.list_all()
    # Opção "mkdir"
        # Cria um novo diretório
    if command == "mkdir":
        user_option = user_input.split(" ")
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
    if command == "rmdir":
        remove_dir_name = user_input.split(" ")[1]
        if remove_dir_name not in ext4._sub_dir:
            print("Dir does not exist")
        else:
            ext4.delete_directory(remove_dir_name)
    # Opção "cp"
        # Faz uma cópia do arquivo para um novo diretório
    if command == "cp":
        file_name = user_input.split(" ")[1]
        dir_name = user_input.split(" ")[2]
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
    if  command == "mv":
        file_name = user_input.split(" ")[1]
        dir_name = user_input.split(" ")[2]
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
    if command == "help":
        for option in options:
            print(" " + option)
    # Opção "test"
    if command == "test":
        if len(user_input.split(" ")) <= 1:
            print("Command not found. Type `help' to see command list")            
        else: 
            input_treat(user_input)
    # Opção "exit"
        # Fecha o programa
    if command == "exit":
        break
        exit()
