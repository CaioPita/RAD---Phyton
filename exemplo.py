def exemplo_01 ():
    arquivo = open('RAD/aula03/manipulando_arquivo/dados.txt')

    print('Nome do arquivo:', arquivo.name)
    print('Tamanho do arquivo:', arquivo.tell())
    print('Modo do arquivo:', arquivo.mode)
    print('Arquivo esta fechado?', arquivo.closed)

    arquivo.close()

    print('Arquivo esta fechado?', arquivo.closed)

def exemplo_02():
    arquivo = open('RAD/aula03/manipulando_arquivo/nomes.txt', 'w')
    arquivo.write('Guilherme')
    arquivo.close()

    arquivo = open('RAD/aula03/manipulando_arquivo/nomes.txt')
    print(arquivo.readline())
    arquivo.close()

def exemplo_03():
    caminho_arquivo = 'RAD/aula03/manipulando_arquivo/nomes.txt'

    arquivo = open(caminho_arquivo, 'r')

    linha1 = arquivo.readline()
    print(f'Linha 1: {linha1}')
    linha2 = arquivo.readline()
    print(f'Linha 2: {linha2}')

    arquivo.close()

def exemplo_04():
    caminho_arquivo =  'RAD/aula03/manipulando_arquivo/nomes.txt'

    arquivo = open(caminho_arquivo, 'r')
    linhas = arquivo.readline()
    for i, linha in enumerate (linhas, start=1):
        print(f'Linha {i}: {linha}')

def exemplo_05():
    caminho_arquivo =  'RAD/aula03/manipulando_arquivo/nomes.txt'

arquivo = open("nomes.txt", 'w')
arquivo.write("Raphael")
arquivo.writelines([""]) 