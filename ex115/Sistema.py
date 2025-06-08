from ex115.lib.interface import *
from time import sleep
while True:
 resposta = menu(['CRIAR ARQUIVOS', 'LISTAR ARQUIVOS', 'EDITAR ARQUIVOS', 'EXCLUIR ARQUIVOS', 'SAIR DO PROGRAMA'])
 if resposta == 1:
     cabeçalho('Opção 1')
 elif resposta == 2:
     cabeçalho('Opção 2')
 elif resposta == 3:
     cabeçalho('Opção 3')
 elif resposta == 4:
     cabeçalho('Opção 4')
 elif resposta == 5:
     cabeçalho(' Saindo do sistema... Até logo!')
     break
 else:
     print('\033[31mError! Digite uma opção válida! \033[m')
 sleep(2)





