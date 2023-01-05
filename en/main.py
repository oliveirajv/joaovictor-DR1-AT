from directory import Directory

def getDir(caminho, caminho_relativo):
    # Este método busca se há o caminho de diretórios 
    # formado pelos elementos da lista "caminho" passada como parâmetro.
    # O parâmetro booleano "caminho_relativo" especifica se os
    # elementos da lista devem ser buscados em caminhos
    # relativos ao diretório atual (dir1/...) ou a partir da raiz (/dir1/...)
    # Caso o caminho não seja encontrado, a função retorna None
    # Caso contrário, é retornado o objeto Diretorio do final do caminho
        if (caminho_relativo):
            prox_dir = atual_directory
        else:
            prox_dir = root_directory        
        ## Enquanto for possível descer na árvore, pega o próximo
        ## diretório do caminho especificado
        for d in caminho:
            if (prox_dir.temFilho(d)):
                prox_dir = prox_dir.getSubDir(d)
            else:
                return None            
        return prox_dir
# Criando o diretório raiz
root_directory = Directory("/")
# Armazenando o diretório atual na variáriavel "atual_directory"
atual_directory = root_directory
# Tupla com as opções disponíveis para o usuário
options = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "cd", "help", "exit")
# Fazendo um while que termina quando o usuário escolha a opção "exit"
while True:
    # Criando um input para o usuário escolher as opções
    user_input = input("joao@victor:" + atual_directory.getCompleteName() + "$ ")
    command = user_input.split(" ")[0]
    # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
    while command not in options:
        print("Command not found. Type `help' to see command list")
        break
    # Opção "new"
        # Cria um arquivo
    if command == "new":
        file_name = user_input.split(" ")[1]
        root_directory.create_file(file_name)
    # Opção "del"
        # Exlcui um arquivo
    if command == "del":
        remove_file_name = user_input.split(" ")[1]
        if file_name not in root_directory._dir_files:
            print("File does not exist")
        else:
            del root_directory._dir_files[remove_file_name]
    # Opção "ls"
        # Mostra todo o conteúdo dos diretórios
    if command == "ls":        
        atual_directory.list_all()
    # Opção "mkdir"
        # Cria um novo diretório
    if command == "mkdir":
        user_option = user_input.split(" ")[1]
        caminho = user_option.split('/')
        
        novo_dir = caminho.pop()

        if user_option[0] == '/':
            caminho_relativo = False
            ## Removendo o primeiro elemento vazio da lista
            caminho.pop(0)
            local = getDir(caminho, caminho_relativo)
        else:
            caminho_relativo = True
            if len(caminho) == 0:      
                local = atual_directory
            else:
                local = getDir(caminho, caminho_relativo)        
        local.make_sub_dir(novo_dir)            
    # Opção "rmdir"
        # Remove o diretório selecionado
    if command == "rmdir":
        remove_dir_name = user_input.split(" ")[1]
        if remove_dir_name not in root_directory._sub_dir:
            print("Dir does not exist")
        else:
            root_directory.delete_sub_dir(remove_dir_name)
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
        caminho = user_option.split('/')          

        if user_option[0] == '/':
            caminho_relativo = False
            ## Removendo o primeiro elemento vazio da lista
            caminho.pop(0)
            atual_directory = getDir(caminho, caminho_relativo)
        else:
            caminho_relativo = True
            if len(caminho) == 0:      
                pass
            else:
                atual_directory = getDir(caminho, caminho_relativo)
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
