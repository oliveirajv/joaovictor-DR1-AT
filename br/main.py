from classe_diretorio import Diretorio

def obter_diretorio(caminho, caminho_relativo):
    # Este método busca se há o caminho de diretórios 
    # formado pelos elementos da lista "caminho" passada como parâmetro.
    # O parâmetro booleano "caminho_relativo" especifica se os
    # elementos da lista devem ser buscados em caminhos
    # relativos ao diretório atual (dir1/...) ou a partir da raiz (/dir1/...)
    # Caso o caminho não seja encontrado, a função retorna None
    # Caso contrário, é retornado o objeto Diretorio do final do caminho
        if (caminho_relativo):
            prox_dir = diretorio_atual
        else:
            prox_dir = diretorio_raiz        
        # Enquanto for possível descer na árvore, pega o próximo
        # diretório do caminho especificado
        for d in caminho:
            if (prox_dir.tem_filho(d)):
                prox_dir = prox_dir.obter_sub_dir(d)
            else:
                return None            
        return prox_dir
# Criando o diretório raiz
diretorio_raiz = Diretorio("/")
# Armazenando o diretório atual na variáriavel "diretorio_atual"
diretorio_atual = diretorio_raiz
# Tupla com as opções disponíveis para o usuário
comandos = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "cd", "help", "exit")
# Fazendo um while que termina quando o usuário escolha a opção "exit"
while True:
    # Criando um input para o usuário escolher as opções
    usuario_input = input("joao@victor:" + diretorio_atual.obter_caminho_completo() + "$ ")
    comando = usuario_input.split(" ")[0]
    # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
    while comando not in comandos:
        print("Command not found. Type `help' to see command list")
        break
    # Opção "new"
        # Cria um arquivo
    if comando == "new":
        arquivo_nome = usuario_input.split(" ")[1]
        diretorio_raiz.criar_arquivo(arquivo_nome)
    # Opção "del"
        # Exlcui um arquivo
    if comando == "del":
        remover_arquivo_nome = usuario_input.split(" ")[1]
        if arquivo_nome not in diretorio_raiz._dir_arquivos:
            print("File does not exist")
        else:
            del diretorio_raiz._dir_arquivos[remover_arquivo_nome]
    # Opção "ls"
        # Mostra todo o conteúdo dos diretórios
    if comando == "ls":        
        diretorio_atual.listar_conteudo()
    # Opção "mkdir"
        # Cria um novo diretório
    if comando == "mkdir":
        usuario_opcao = usuario_input.split(" ")[1]
        caminho = usuario_opcao.split('/')
        
        novo_dir = caminho.pop()

        if usuario_opcao[0] == '/':
            caminho_relativo = False
            ## Removendo o primeiro elemento vazio da lista
            caminho.pop(0)
            local = obter_diretorio(caminho, caminho_relativo)
        else:
            caminho_relativo = True
            if len(caminho) == 0:      
                local = diretorio_atual
            else:
                local = obter_diretorio(caminho, caminho_relativo)        
        local.criar_sub_diretorio(novo_dir)            
    # Opção "rmdir"
        # Remove o diretório selecionado
    if comando == "rmdir":
        remover_diretorio_nome = usuario_input.split(" ")[1]
        if remover_diretorio_nome not in diretorio_raiz._sub_dir:
            print("Dir does not exist")
        else:
            diretorio_raiz.deletar_sub_dir(remover_diretorio_nome)
    # Opção "cp"
        # Faz uma cópia do arquivo para um novo diretório
    if comando == "cp":
        arquivo_nome = usuario_input.split(" ")[1]
        dir_name = usuario_input.split(" ")[2]
        if arquivo_nome not in diretorio_raiz._dir_arquivos:
            print("File does not exist")
        elif dir_name not in diretorio_raiz._sub_dir:
            print("Dir does not exist")
        else:
            dir = diretorio_raiz.get_directory(dir_name)
            copia_arquivo_valor = diretorio_raiz._dir_arquivos.get(arquivo_nome)
            dir._dir_arquivos[arquivo_nome] = copia_arquivo_valor
    # Opção "mv"
        # Move o arquivo para um novo diretório e exclui do anterior
    if  comando == "mv":
        arquivo_nome = usuario_input.split(" ")[1]
        dir_name = usuario_input.split(" ")[2]
        if arquivo_nome not in diretorio_raiz._dir_arquivos:
            print("File does not exist") 
        elif dir_name not in diretorio_raiz._sub_dir:
            print("Dir does not exist")        
        else:
            copia_arquivo_valor = diretorio_raiz._dir_arquivos.get(arquivo_nome)
            dir = diretorio_raiz.get_directory(dir_name)
            dir._dir_arquivos[arquivo_nome] = copia_arquivo_valor            
            del diretorio_raiz._dir_arquivos[arquivo_nome]
    # Opção "cd"
        # Possibilita a movimentação entre diretórios
    if comando == "cd":
        usuario_opcao = usuario_input.split(" ")[1]
        caminho = usuario_opcao.split('/')          

        if usuario_opcao[0] == '/':
            caminho_relativo = False
            # Removendo o primeiro elemento vazio da lista
            caminho.pop(0)
            diretorio_atual = obter_diretorio(caminho, caminho_relativo)
        else:
            caminho_relativo = True
            if len(caminho) == 0:      
                pass
            else:
                diretorio_atual = obter_diretorio(caminho, caminho_relativo)
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
