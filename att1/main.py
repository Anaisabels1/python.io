# from src.sua_classe import seu_manipulador_de_texto
from src.sua_classe import SuaClasse

def main():
    leitor = SuaClasse("exemplo.txt")  # substitua pelo nome real do arquivo

    print(f"\n Total de palavras no texto: {len(leitor)}")

    print("\n Palavras que começam com 'a':")
    print(leitor.filtrar_por_inicio('a'))

    print("\n Palavras que contêm 'e':")
    print(leitor.filtrar_contem_letra('e'))

    print("\n Texto com vírgulas substituídas por pontos:")
    print(leitor.substituir_virgulas_por_pontos())

    print("\n Datas encontradas no texto:")
    print(leitor.extrair_datas())

    print("\n Texto com informações sensíveis ocultadas:")
    print(leitor.ocultar_info_sensivel())

if __name__ == "_main_":
    main()