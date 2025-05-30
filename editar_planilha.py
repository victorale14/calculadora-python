'''

23 a biblioteca openpyxl serve para ler e escrever excel 2010 em arquivos xlsx/xlsm,
segundo o próprio site (https://openpyxl.readthedocs.io/en/stable/index.html)
workbook é o que seria a planilha excel, portanto, a funcionalidade load_workbook se trata de carregar a planilha 

(esse código funciona presumindo que o usuário leu anteriormente a planilha)

25 e 26 primeiro, pega-se o input do nome do arquivo que se deseja editar e tenta-se abrir ele
27 e 47 caso não consiga por causa de erro em localizar o arquivo, avisa que não foi possível encontrar o arquivo e o código para.
28 adiciona a extensão ".xlsx" junto do nome do arquivo com uma f-string
29 wb é declarado como a função que carrega o arquivo, para fins de simplificação
30 a planilha é definida como o ativo de wb, ou seja, a a planilha que está sendo carregada está sendo definida como ativa
31 - 35 são printados os avisos e o input do texto que será mudado é pego, assim como o texto que será posto no local do antigo
36 define a variável que diz se o texto foi ou não alterado
37 - 39 checa a fileira e as 'células' nas fileiras, chegando por coluna na direção horizontal, quando acaba passa para a próxima linha na direção vertical
40 - 41 caso o valor presente na célula seja igual ao texto que se quer mudar, ele muda o texto para o definido anteriormente
42 - 43 a planilha é salva e alterado é definido para verdadeiro
44 - 45 se alterado for verdadeiro, avisa que foi um sucesso, se for falso, avisa que que o termo não foi achado.

'''

from openpyxl import load_workbook

print('Qual o nome do arquivo que você gostaria de editar?')
nome_arquivo = input('Digite o nome do arquivo: ')
try:
    arquivo = f'{nome_arquivo}.xlsx'
    wb = load_workbook(arquivo)
    planilha = wb.active
    print(f'Arquivo {arquivo} carregado com sucesso!')
    print('Qual texto gostaria de mudar?')
    texto = input('> ')
    print(f'Digite o que gostaria de pôr no lugar de {texto}')
    mudar = input('> ')
    alterado = False
    for fileira in planilha:
        for celula in fileira:
            valor = celula.value
            if valor == texto:
                valor = mudar
                wb.save(arquivo)
                alterado = True
    if alterado: print('O documento foi alterado e salvo com sucesso! Recomendo que feche e abra o arquivo.')
    else: print('Não foi possível alterar o documento. O termo a ser mudado não foi encontrado, tente novamente.')

except FileNotFoundError:
    print(f'O arquivo {nome_arquivo} não foi encontrado. Verifique o nome e tente novamente.')