from os import getenv, chdir, mkdir, rmdir, listdir, getcwd, remove
from shutil import copy
from distutils.dir_util import copy_tree
try:
    # Pegando usuário
    input_usuario = input("USUÁRIO ")    
    # Pegando senha
    input_senha = input("SENHA ")
except KeyboardInterrupt:
    print("\nProgram ended by keyboard interruption")
    exit()
# Autenticando o usário
def authenticate(usuario, password):
    usuario_autorizado = getenv("USER")
    if (usuario != usuario_autorizado):
        return False
    senha_autorizada = getenv("PASSWORD")
    if (password != senha_autorizada):
        return False
    return True    
if (authenticate(input_usuario, input_senha)):
    login = True
    print("Login successfully")
else:
    login = False
    print("Access denied")
# Pegando o diretório "HOME"
diretorio_home = getenv("HOMEDIR")
# Passando o path do programa para o diretório "home_dir"
chdir(diretorio_home)
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
        try:
            # Opção "new"
                # Cria um arquivo
            if comando == "new":    
                arquivo_nome = usuario_input.split(" ")[1] 
                open(arquivo_nome, "x")
            # Opção "del"
                # Exlcui um arquivo
            if comando == "del":         
                arquivo_nome = usuario_input.split(" ")[1] 
                remove(arquivo_nome)
            # Opção "ls"
                # Mostra todo o conteúdo dos diretórios
            if comando == "ls":
                for item in listdir(diretorio_atual):
                    print(" " , item)
            # Opção "mkdir"
                # Cria um novo diretório
            if comando == "mkdir":          
                diretorio_nome = usuario_input.split(" ")[1] 
                mkdir(diretorio_nome)
            # Opção "rmdir"
                # Remove o diretório selecionado
            if comando == "rmdir":
                diretorio_nome = usuario_input.split(" ")[1]
                rmdir(diretorio_nome)
            # Opção "cp"
                # Faz uma cópia do arquivo para um novo diretório
            if comando == "cp": 
                arquivo_nome = usuario_input.split(" ")[1]
                destino = usuario_input.split(" ")[2]
                copy(arquivo_nome, destino)
            # Opção "mv"
                # Move o arquivo para um novo diretório e exclui do anterior
            if comando == "mv":
                arquivo_nome = usuario_input.split(" ")[1]
                destino = usuario_input.split(" ")[2]
                copy(arquivo_nome, destino)
                remove(arquivo_nome)
            # Opção "cd"
                # Possibilita a movimentação entre diretórios
            if comando == "cd":
                destino = usuario_input.split(" ")[1]
                chdir(destino) # Mudando o diretório atual para o destino
                destino = getcwd() # armazenando o diretório atual na variável destino
                diretorio_atual = destino                
            # Opção "backup"
                # Guarda o conteúdo que tem no caminho ("path") que o usuário está
            if comando == "backup":
                # Guardando em uma variável o conteúdo da variável local, que é o caminho aonde os itens serão armazenados
                backup_path = getenv("INFNET_BACKUP")
                copy_tree(diretorio_atual, backup_path)
            # Opção "help"
                # Mostra os comandos disponíveis
            if comando == "help":
                for item in comandos:
                    print(" " , item)
            # Opção "exit"
                # Fecha o programa
            if comando == "exit":
                break
                exit()         
        except FileExistsError:
            print("File or Directory already exists")
        except FileNotFoundError:
            print("File or Directory not found")
        except OSError:
            print("Path name is incorrect")
        except IndexError:
            print("Incorrect command")
    except KeyboardInterrupt:
            print("\nProgram ended by keyboard interruption")
            break
            exit()
