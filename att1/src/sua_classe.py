# IMPORTANTE: RENOMEIE ESSE ARQUIVO PARA O NOME QUE VOCE QUISER
# DEFINA SUA CLASSE AQUI E EXECUTE ELA NO MAIN.PY POR MEIO DE IMPORTS
import re
from typing import List


class SuaClasse:
    """
    Classe para processar arquivos de texto usando expressões regulares.
    """

    def _init_(self, caminho_arquivo: str):
        """
        Inicializa o objeto com o conteúdo de um arquivo .txt.
        """
        self.caminho_arquivo = caminho_arquivo
        self.conteudo = self._ler_arquivo()

    def _ler_arquivo(self) -> str:
        """
        Lê e retorna o conteúdo do arquivo.
        """
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()

    def filtrar_por_inicio(self, letra: str) -> List[str]:
        """
        Retorna palavras que começam com a letra especificada.
        """
        return re.findall(rf'\b{letra}\w*', self.conteudo, flags=re.IGNORECASE)

    def filtrar_contem_letra(self, letra: str) -> List[str]:
        """
        Retorna palavras que contêm a letra especificada em qualquer posição.
        """
        return re.findall(rf'\b\w*{letra}\w*\b', self.conteudo, flags=re.IGNORECASE)

    def substituir_virgulas_por_pontos(self) -> str:
        """
        Retorna o texto com vírgulas substituídas por pontos.
        """
        return self.conteudo.replace(',', '.')

    def extrair_datas(self) -> List[str]:
        """
        Retorna uma lista de datas no formato DD/MM/AAAA ou DD-MM-AAAA.
        """
        return re.findall(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b', self.conteudo)

    def ocultar_info_sensivel(self) -> str:
        """
        Retorna o texto com e-mails, CPFs e telefones ocultados.
        """
        texto = self.conteudo
        texto = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[EMAIL_OCULTO]', texto)
        texto = re.sub(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b', '[CPF_OCULTO]', texto)
        texto = re.sub(r'\b\d{2} ?\d{4,5}-?\d{4}\b', '[TEL_OCULTO]', texto)
        return texto

    def _len_(self) -> int:
        """
        Dunder Method: Retorna o número de palavras no texto.
        """
        return len(re.findall(r'\b\w+\b', self.conteudo))