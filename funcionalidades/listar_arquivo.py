import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def listar():
    diretorio = filedialog.askdirectory(title="Selecione uma pasta")

    extensoes_excel = (".xlsx", ".xls")

    if diretorio:
        print(f"Listando arquivos Excel em: {diretorio}\n")

        for pasta_atual, subpastas, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                if arquivo.lower().endswith(extensoes_excel):
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    print(caminho_completo)
    else:
        print("Nenhum diretório foi selecionado.")
