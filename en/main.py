from class_directory import Directory

def get_dir(path, relative_path):
    # Este método busca se há o path de diretórios 
    # formado pelos elementos da lista "path" passada como parâmetro.
    # O parâmetro booleano "relative_path" especifica se os
    # elementos da lista devem ser buscados em paths
    # relativos ao diretório atual (dir1/...) ou a partir da raiz (/dir1/...)
    # Caso o path não seja encontrado, a função retorna None
    # Caso contrário, é retornado o objeto Diretorio do final do path
        if (relative_path):
            next_directory = atual_directory
        else:
            next_directory = root_directory        
        # Enquanto for possível descer na árvore, pega o próximo
        # diretório do path especificado
        for directory in path:
            if (next_directory.has_child(directory)):
                next_directory = next_directory.get_sub_dir(directory)
            else:
                return None            
        return next_directory
# Criando o diretório raiz
root_directory = Directory("/")
# Armazenando o diretório atual na variáriavel "atual_directory"
atual_directory = root_directory
# Tupla com as opções disponíveis para o usuário
options = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "cd", "help", "exit")
# Fazendo um while que termina quando o usuário escolha a opção "exit"
while True:
    # Criando um input para o usuário escolher as opções
    user_input = input(f"joao@victor:{atual_directory.get_complete_name()}$ ")
    command = user_input.split(" ")[0]
    # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
    while command not in options:
        print("Command not found. Type `help' to see command list")
        break
    # Opção "new"
        # Cria um arquivo
    if command == "new":
        user_option = user_input.split(" ")[1]
        path = user_option.split('/')
        
        new_file_name = path.pop()

        if user_option[0] == '/':
            relative_path = False
            # Removendo o primeiro elemento vazio da lista
            path.pop(0)
            local = get_dir(path, relative_path)
        else:
            relative_path = True
            if len(path) == 0:      
                local = atual_directory
            else:
                local = get_dir(path, relative_path)  
        local.create_file(new_file_name)
    # Opção "del"
        # Exlcui um arquivo
    if command == "del":
        user_option = user_input.split(" ")[1]
        path = user_option.split('/')
        
        delete_file_name = path.pop()

        if user_option[0] == '/':
            relative_path = False
            # Removendo o primeiro elemento vazio da lista
            path.pop(0)
            local = get_dir(path, relative_path)
        else:
            relative_path = True
            if len(path) == 0:      
                local = atual_directory
            else:
                local = get_dir(path, relative_path)  
        local.delete_file(delete_file_name)
    # Opção "ls"
        # Mostra todo o conteúdo dos diretórios
    if command == "ls":        
        atual_directory.list_all()
    # Opção "mkdir"
        # Cria um novo diretório
    if command == "mkdir":
        user_option = user_input.split(" ")[1]
        path = user_option.split('/')
        
        create_directory_name = path.pop()

        if user_option[0] == '/':
            relative_path = False
            # Removendo o primeiro elemento vazio da lista
            path.pop(0)
            local = get_dir(path, relative_path)
        else:
            relative_path = True
            if len(path) == 0:      
                local = atual_directory
            else:
                local = get_dir(path, relative_path)  
        local.make_sub_dir(create_directory_name)            
    # Opção "rmdir"
        # Remove o diretório selecionado
    if command == "rmdir":
        user_option = user_input.split(" ")[1]
        path = user_option.split('/')
        
        delete_directory_name = path.pop()

        if user_option[0] == '/':
            relative_path = False
            # Removendo o primeiro elemento vazio da lista
            path.pop(0)
            local = get_dir(path, relative_path)
        else:
            relative_path = True
            if len(path) == 0:      
                local = atual_directory
            else:
                local = get_dir(path, relative_path)  
        local.delete_sub_dir(delete_directory_name)
    # Opção "cp"
        # Faz uma cópia do arquivo para um novo diretório
    if command == "cp":
        file_name = user_input.split(" ")[1]
        dir_name = user_input.split(" ")[2]
        if file_name not in root_directory._dir_files:
            print("File does not exist")
        elif dir_name not in root_directory._sub_dir:
            print("Dir does not exist")
        else:
            dir = root_directory.get_directory(dir_name)
            copy_file_value = root_directory._dir_files.get(file_name)
            dir._dir_files[file_name] = copy_file_value
    # Opção "mv"
        # Move o arquivo para um novo diretório e exclui do anterior
    if  command == "mv":
        file_name = user_input.split(" ")[1]
        dir_name = user_input.split(" ")[2]
        if file_name not in root_directory._dir_files:
            print("File does not exist") 
        elif dir_name not in root_directory._sub_dir:
            print("Dir does not exist")        
        else:
            copy_file_value = root_directory._dir_files.get(file_name)
            dir = root_directory.get_directory(dir_name)
            dir._dir_files[file_name] = copy_file_value            
            del root_directory._dir_files[file_name]
    # Opção "cd"
        # Possibilita a movimentação entre diretórios
    if command == "cd":
        user_option = user_input.split(" ")[1]
        path = user_option.split('/')          

        if user_option[0] == '/':
            relative_path = False
            # Removendo o primeiro elemento vazio da lista
            path.pop(0)
            atual_directory = get_dir(path, relative_path)
        else:
            relative_path = True
            if len(path) == 0:      
                pass
            else:
                atual_directory = get_dir(path, relative_path)
    # Opção "help"
        # Mostra os comandos disponíveis
    if command == "help":
        for option in options:
            print(" " , option)
    # Opção "exit"
        # Fecha o programa
    if command == "exit":
        break
        exit()
