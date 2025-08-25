from funcionalidades.modulos import *

root = tk.Tk()
root.withdraw()

def listar(pasta):
    extensoes_excel = (".xlsx", ".xls")

    if pasta:
        print(f"Listando arquivos Excel em: {pasta}\n")

        for pasta_atual, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                if arquivo.lower().endswith(extensoes_excel):
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    print(caminho_completo)
    else:
        print("Nenhum diretório foi selecionado.")