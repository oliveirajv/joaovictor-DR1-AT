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
        for diretorio in caminho:
            if (prox_dir.tem_filho(diretorio)):
                prox_dir = prox_dir.obter_sub_dir(diretorio)
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
    usuario_input = input(f"joao@victor:{diretorio_atual.obter_caminho_completo()}$ ")
    comando = usuario_input.split(" ")[0]
    # Fazendo um while para dizer que a opção não existe, enquanto o usuário não escreve uma opção dentre as existentes
    while comando not in comandos:
        print("Command not found. Type `help' to see command list")
        break
    # Opção "new"
        # Cria um arquivo
    if comando == "new":
        usuario_opcao = usuario_input.split(" ")[1]
        caminho = usuario_opcao.split('/')
        
        novo_arquivo_nome = caminho.pop()

        if usuario_opcao[0] == '/':
            caminho_relativo = False
            # Removendo o primeiro elemento vazio da lista
            caminho.pop(0)
            local = obter_diretorio(caminho, caminho_relativo)
        else:
            caminho_relativo = True
            if len(caminho) == 0:      
                local = diretorio_atual
            else:
                local = obter_diretorio(caminho, caminho_relativo)  
        local.criar_arquivo(novo_arquivo_nome)
    # Opção "del"
        # Exlcui um arquivo
    if comando == "del":
        usuario_opcao = usuario_input.split(" ")[1]
        caminho = usuario_opcao.split('/')
        
        arquivo_deletar = caminho.pop()

        if usuario_opcao[0] == '/':
            caminho_relativo = False
            # Removendo o primeiro elemento vazio da lista
            caminho.pop(0)
            local = obter_diretorio(caminho, caminho_relativo)
        else:
            caminho_relativo = True
            if len(caminho) == 0:      
                local = diretorio_atual
            else:
                local = obter_diretorio(caminho, caminho_relativo)        
        local.deletar_arquivo(arquivo_deletar)
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
            # Removendo o primeiro elemento vazio da lista
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
        usuario_opcao = usuario_input.split(" ")[1]
        caminho = usuario_opcao.split('/')
        
        diretorio_deletar = caminho.pop()

        if usuario_opcao[0] == '/':
            caminho_relativo = False
            # Removendo o primeiro elemento vazio da lista
            caminho.pop(0)
            local = obter_diretorio(caminho, caminho_relativo)
        else:
            caminho_relativo = True
            if len(caminho) == 0:      
                local = diretorio_atual
            else:
                local = obter_diretorio(caminho, caminho_relativo)  
        local.deletar_sub_dir(diretorio_deletar)
    # Opção "cp"
        # Faz uma cópia do arquivo para um novo diretório
    if comando == "cp":
        pass
    # Opção "mv"
        # Move o arquivo para um novo diretório e exclui do anterior
    if  comando == "mv":
        pass
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
