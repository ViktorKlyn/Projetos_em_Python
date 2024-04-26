from desafio import menu, cabecalho
from teste import arquivo_existe, criar_arquivo, ler_arquivo, cadastrar
from time import sleep

arquivo = 'nomes.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    
    if resposta == 1:
        ler_arquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
        
    sleep(2)