import shutil;
from tkinter.filedialog import askdirectory;
arq_ex = askdirectory(title="Selecione o arquivo Excel que deseja excluir");
try:
    shutil.rmtree(arq_ex);
    print(f"Arquivo {arq_ex} excluído com sucesso!");
except FileNotFoundError:
    print(f"Erro: Arquivo {arq_ex} não encontrado.");
