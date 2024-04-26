from desafio import cabecalho
def arquivoExiste(nome):
    try:
        with open(nome, 'rt') as a:
            pass
    except FileNotFoundError:
        return False
    return True

def criarArquivo(nome):
    try:
        with open(nome, 'wt+') as a:
            pass
    except Exception as e:
        print(f'Houve um ERRO na criação do arquivo: {e}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        with open(nome, 'rt') as a:
            cabecalho('Pessoas cadastradas')  # Assuming you have the necessary function defined elsewhere
            for linha in a:
                dado = linha.strip().split(';')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at') as a:
            a.write(f'{nome};{idade}\n')
    except Exception as e:
        print(f'Houve um ERRO na hora de escrever os dados: {e}')
    else:
        print(f'Novo registro de {nome} adicionado')
        a.close()
