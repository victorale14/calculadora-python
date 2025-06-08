import os;
import shutil;
from tkinter.filedialog import askdirectory;
nome_do_arquivo = askdirectory(title="Selecione o arquivo Excel que deseja excluir");
try:
    shutil.rmtree(nome_do_arquivo);
    print(f"Arquivo {nome_do_arquivo} excluído com sucesso!");
except FileNotFoundError:
    print(f"Erro: Arquivo {nome_do_arquivo} não encontrado.");
