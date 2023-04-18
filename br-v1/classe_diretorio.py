from random import randrange
from colored import fg, attr
class Diretorio:
    def __init__(self, _dir_nome, _dir_pai = None):
        self._dir_nome = _dir_nome
        # Conteúdo do diretório
        self._dir_arquivos = {}
        self._sub_dir = {}
        self._dir_pai = _dir_pai
    # Pega o diretório pai
    def obter_pai(self):
        return self._dir_pai
    # Pega todos os diretórios até o que o usuário está
    def obter_caminho_completo(self):
        caminho_completo = [self._dir_nome]
        pai = self.obter_pai()

        while (pai != None):            
            caminho_completo.insert(0, pai._dir_nome)
            pai = pai.obter_pai()        
        resultado = ''
        if len(caminho_completo) > 1:
            for i,dir in enumerate(caminho_completo):
                if (i == 0):
                    resultado += dir
                else:
                    resultado += dir + '/'
        else:
            resultado = '/'
        return resultado
    # Pega diretório
    def obter_diretorio(self, _dir_nome):
        diretorio = self._sub_dir[_dir_nome]
        return diretorio
    # Verifica se tem filho
    def tem_filho(self, _sub_dir):
        if (_sub_dir != '..'):
            if (_sub_dir in self._sub_dir):
                return True
            return False
        return True
    # Pega o sub diretório
    def obter_sub_dir(self, _sub_dir):
        if (_sub_dir != '..'):
            if (self.tem_filho(_sub_dir)):
                return self._sub_dir.get(_sub_dir)
            return None
        return self._dir_pai
    # Cria arquivo
    def criar_arquivo(self, _arquivo_nome):
        _arquivo_tamanho = randrange(1, 8096)
        self._dir_arquivos[_arquivo_nome] = _arquivo_tamanho
    # Deleta arquivo
    def deletar_arquivo(self, _arquivo_nome):
        del self._dir_arquivos[_arquivo_nome]
    # Lista conteúdo do diretório
    def listar_conteudo(self):
        cor = fg("slate_blue_1")
        resetar = attr("reset")
        for items in self._dir_arquivos:
            print(" " , items , self._dir_arquivos[items])
        for items in self._sub_dir:
            print(cor , items , self._sub_dir[items] , resetar)
    # Cria sub diretório
    def criar_sub_diretorio(self, _sub_dir):
        diretorio = Diretorio(_sub_dir, self)
        self._sub_dir[diretorio._dir_nome] = diretorio
    # Deleta sub diretório
    def deletar_sub_dir(self, _dir_nome):
        del self._sub_dir[_dir_nome]    
    # Copia arquivo
    def copiar_arquivo(self, _arquivo_nome, _dir_nome):
        pass
    # Move arquivo
    def mover_arquivo(self, _arquivo_nome, _dir_nome):
        arquivo_tamanho = self._dir_arquivos.get(_arquivo_nome)
        _dir_nome._dir_arquivos[_arquivo_nome] = arquivo_tamanho 
        del self._dir_arquivos[_arquivo_nome]
    # Mostrando a classe Diretorio formatado
    def __str__(self):
        return str(self._dir_nome) + str(self._dir_arquivos) + str(self._sub_dir)
