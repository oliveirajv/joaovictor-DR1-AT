from os import getenv, chdir, mkdir, rmdir, listdir, getcwd, remove
from shutil import copy
from distutils.dir_util import copy_tree
try:    
    input_usuario = input("USUÁRIO ")# Pegando usuário    
    input_senha = input("SENHA ")# Pegando senha
except KeyboardInterrupt:
        print("\nProgram ended by keyboard interruption")
        exit()
# Pegando o diretório "HOME"
diretorio_home = getenv("INFNET_HOMEDIR")
# Passando o path do programa para o diretório "home_dir"
chdir(diretorio_home)
# Autenticando o usário
def authenticate(usuario, password):
    usuario_autorizado = getenv("INFNET_USER")
    if (usuario != usuario_autorizado):
        return False
    senha_autorizada = getenv("INFNET_PASSWD")
    if (password != senha_autorizada):
        return False
    return True    
if (authenticate(input_usuario, input_senha)):
    login = True
    print("Login successfully")
else:
    login = False
    print("Access denied")
# Diretório raiz
diretorio_atual = diretorio_home
# Tupla com as opções disponíveis para o usuário
comandos = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "cd", "backup", "help", "exit")
# Fazendo um while que termina quando o usuário escolha a opção "exit"
while login == True:
    try:
        # Criando um input para o usuário escolher as opções
        usuario_input = input(f"{diretorio_atual}> ")
        comando = usuario_input.split(" ")[0]
        # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
        
        while comando not in comandos:
            print("Command not found. Type `help' to see command list")
            break
        # Opção "new"
            # Cria um arquivo
        if comando == "new":
            try:                
                arquivo_nome = usuario_input.split(" ")[1] 
                open(arquivo_nome, "x")          
            except FileExistsError:
                print("File already exists")
            except IndexError:
                print("Incorrect command")
        # Opção "del"
            # Exlcui um arquivo
        if comando == "del":
            try:                
                arquivo_nome = usuario_input.split(" ")[1] 
                remove(arquivo_nome)          
            except OSError:
                print("File does not exists")
            except IndexError:
                print("Incorrect command")
        # Opção "ls"
            # Mostra todo o conteúdo dos diretórios
        if comando == "ls":
            for item in listdir(diretorio_atual):
                print(" " , item)
        # Opção "mkdir"
            # Cria um novo diretório
        if comando == "mkdir":           
            try:                
                diretorio_nome = usuario_input.split(" ")[1] 
                mkdir(diretorio_nome)          
            except FileExistsError:
                print("Directory already exists")
            except IndexError:
                print("Incorrect command")
        # Opção "rmdir"
            # Remove o diretório selecionado
        if comando == "rmdir":
            try:
                diretorio_nome = usuario_input.split(" ")[1]
                rmdir(diretorio_nome)
            except FileNotFoundError:
                print("Directory does not exists")
            except IndexError:
                print("Incorrect command")
        # Opção "cp"
            # Faz uma cópia do arquivo para um novo diretório
        if comando == "cp":
            try:    
                arquivo_nome = usuario_input.split(" ")[1]
                destino = usuario_input.split(" ")[2]
                copy(arquivo_nome, destino)
            except Exception as error:
                print(error)
        # Opção "mv"
            # Move o arquivo para um novo diretório e exclui do anterior
        if  comando == "mv":
            try:
                arquivo_nome = usuario_input.split(" ")[1]
                destino = usuario_input.split(" ")[2]
                copy(arquivo_nome, destino)
                remove(arquivo_nome)
            except Exception as error:
                print(error)
        # Opção "cd"
            # Possibilita a movimentação entre diretórios
        if comando == "cd":
            try:
                destino = usuario_input.split(" ")[1]
                chdir(destino) # Mudando o diretório atual para o destino
                destino = getcwd() # armazenando o diretório atual na variável destino
                diretorio_atual = destino
            except FileNotFoundError:
                print("Path not found")
            except OSError:
                print("Path name is incorrect")
            except IndexError:
                print("Incorrect command")
        # Opção "backup"
            # Guarda o conteúdo que tem no caminho ("path") que o usuário está
        if comando == "backup":
            # Guardando em uma variável o conteúdo da variável local, que é o caminho aonde os itens serão armazenados
            backup_path = getenv("INFNET_BACKUP")
            copy_tree(diretorio_atual, backup_path)
        # Opção "help"
            # Mostra os comandos disponíveis
        if comando == "help":
            for comando in comandos:
                print(" " , comando)
        # Opção "exit"
            # Fecha o programa
        if comando == "exit":
            break
            exit()            
    except OSError:
            print("The filename, directory name, or volume label syntax is incorrect")
    except KeyboardInterrupt:
            print("\nProgram ended by keyboard interruption")
            break
            exit()