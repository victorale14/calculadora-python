from funcionalidades.modulos import *

def excluir(pasta):
    try:
        shutil.rmtree(pasta)
        print(f"Arquivo {pasta} excluído com sucesso!")
    except FileNotFoundError:
        print(f"Erro: Arquivo {pasta} não encontrado.")
