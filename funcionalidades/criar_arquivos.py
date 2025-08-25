from funcionalidades.modulos import *

def criar(pasta):
    print('criar planilha')
    wb = Workbook()
    arquivo = wb.active
    colunas = int(input('Quantas colunas a planilha terá?\n >'))
    if 0 >= colunas > 26:
        return f'Uma planilha não pode ter mais que 26 colunas ou menos que uma! {colunas} não é um número aceitável.'
    linhas = int(input('Quantas linhas a planilha terá?\n >'))
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    y = 0
    while y != colunas:
        x = 0
        while x != linhas:
            arquivo[f'{alfabeto[y]}{x+1}'] = input(f'Digite o que estará na linha {x+1} da coluna {alfabeto[y]}: ')
            x = x + 1
        y = y + 1
    nome_do_arquivo = input('Digite o nome que gostaria de dar ao arquivo: ')
    wb.save(f'{pasta}\{nome_do_arquivo}.xlsx')