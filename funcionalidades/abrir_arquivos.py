from funcionalidades.modulos import *

def abrir_planilha(pasta):
    """
    Permite ao usuário selecionar uma pasta e o nome de um arquivo Excel,
    e então abre o arquivo para imprimir seu conteúdo.
    """
    # Inicializa o Tkinter, mas esconde a janela principal que não será usada
    root = tk.Tk()
    root.withdraw()

    print(f"Pasta selecionada: {pasta}")

    # Pede o nome do arquivo Excel
    nome_arquivo = input("Qual o nome do arquivo Excel que você quer abrir? (sem .xlsx): ")
    if not nome_arquivo:
        print("Nenhum nome de arquivo foi inserido. Operação cancelada.")
        return

    # Constrói o caminho completo para o arquivo
    caminho_completo_arquivo = os.path.join(pasta, f"{nome_arquivo}.xlsx")

    print(f"Tentando abrir o arquivo: {caminho_completo_arquivo}")

    try:
        # Carrega a pasta de trabalho (workbook)
        workbook = openpyxl.load_workbook(caminho_completo_arquivo)

        # Itera sobre todas as planilhas na pasta de trabalho
        for sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]
            print(f"\n--- Planilha: {sheet_name} ---")

            # Itera sobre as linhas e colunas para imprimir o conteúdo das células
            for row in sheet.iter_rows():
                row_values = []
                for cell in row:
                    # Adiciona o valor da célula. Se for None, converte para string vazia para evitar erro de concatenação.
                    row_values.append(str(cell.value if cell.value is not None else ''))
                print("\t".join(row_values)) # Usa tabulação para separar os valores e simular colunas

        print(f"\nO arquivo '{nome_arquivo}.xlsx' foi lido com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_completo_arquivo}' não foi encontrado.")
        print("Verifique se o nome do arquivo está correto e se ele está na pasta selecionada.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir a planilha: {e}")