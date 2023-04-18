from os import getenv, chdir, mkdir, rmdir, listdir, getcwd
try:
    # Pegando usuário
    user_input = input("USER ")
    # Pegando senha
    password_input = input("PASSWORD ")
    # Pegando o diretório "HOME"
    home_dir = getenv("INFNET_HOMEDIR")
    # Passando o path do programa para o diretório "home_dir"
    chdir(home_dir)
    # Autenticando o usário
    def authenticate(user, password):
        user_authorized = getenv("INFNET_USER")
        if (user != user_authorized):
            return False
        password_authorized = getenv("INFNET_PASSWD")
        if (password != password_authorized):
            return False
        return True    
    if (authenticate(user_input, password_input)):
        login = True
        print("Login successfully")
    else:
        login = False
        print("Access denied")
    # Diretório raiz
    atual_directory = home_dir
    # Tupla com as opções disponíveis para o usuário
    options = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "cd", "help", "exit")
    # Fazendo um while que termina quando o usuário escolha a opção "exit"
    while login == True:
        # Criando um input para o usuário escolher as opções
        user_input = input(f"{atual_directory}> ")
        command = user_input.split(" ")[0]
        # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
        while command not in options:
            print("Command not found. Type `help' to see command list")
            break
        # Opção "new"
            # Cria um arquivo
        if command == "new":
            pass
        # Opção "del"
            # Exlcui um arquivo
        if command == "del":
            pass
        # Opção "ls"
            # Mostra todo o conteúdo dos diretórios
        if command == "ls":        
            for item in listdir(atual_directory):
                print(" " , item)
        # Opção "mkdir"
            # Cria um novo diretório
        if command == "mkdir":
            create_dir_name = user_input.split(" ")[1]
            mkdir(create_dir_name)          
        # Opção "rmdir"
            # Remove o diretório selecionado
        if command == "rmdir":
            remove_dir_name = user_input.split(" ")[1]
            rmdir(remove_dir_name)
        # Opção "cp"
            # Faz uma cópia do arquivo para um novo diretório
        if command == "cp":
            pass
        # Opção "mv"
            # Move o arquivo para um novo diretório e exclui do anterior
        if  command == "mv":
            pass
        # Opção "cd"
            # Possibilita a movimentação entre diretórios
        if command == "cd":
            try:
                path = user_input.split(" ")[1]
                chdir(path)
                path = getcwd()
                atual_directory = path
            except FileNotFoundError:
                print("Path not found")
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
except KeyboardInterrupt:
        print("\nProgram ended by keyboard interruption")