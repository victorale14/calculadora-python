from funcionalidades.interface import *
from funcionalidades.abrir_arquivos import abrir_planilha
from funcionalidades.editar_planilha import editar
from funcionalidades.listar_arquivo import listar
from funcionalidades.excluir_planilha import excluir
from funcionalidades.criar_arquivos import criar
from time import sleep
from tkinter.filedialog import askdirectory

pasta = askdirectory(title='Selecione a pasta que será utilizada no programa')

while True:
    resposta = menu(['CRIAR ARQUIVOS', 'ABRIR ARQUIVO','LISTAR ARQUIVOS', 'EDITAR ARQUIVOS', 'EXCLUIR ARQUIVOS', 'SAIR DO PROGRAMA'])
    if resposta == 1:
        cabeçalho('Opção 1')
        criar(pasta)
        sleep(5)
    elif resposta == 2:
        cabeçalho('Opção 2')
        abrir_planilha(pasta)
        sleep(5)
    elif resposta == 3:
        cabeçalho('Opção 3')
        listar(pasta)
        sleep(5)
    elif resposta == 4:
        cabeçalho('Opção 4')
        editar(pasta)
        sleep(5)
    elif resposta == 5:
        cabeçalho('Opção 5')
        excluir(pasta)
        sleep(5)
    elif resposta == 6:
        cabeçalho('Opção 6')
        exit()
    else:
        print('\033[31mError! Digite uma opção válida! \033[m')
        sleep(2)