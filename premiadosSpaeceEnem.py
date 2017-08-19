import pandas as pd
import numpy as np
import operator

arquivo = 'premiados.csv'
df = pd.read_csv(arquivo, sep=';')

def rankingBycolumn(column):
    numberNotebooks = {}
    values = df[column].unique()
    gb = df.groupby(column)

    for value in values:
        numberNotebooks[value] = gb.get_group(value).ALUNO.size
    ranking = sorted(numberNotebooks.items(), key=operator.itemgetter(1), reverse=True)
    return ranking

def main():
    colunas = df.columns.values
    optionBanner(colunas)
    col = choosecolumn(colunas)
    ranking = rankingBycolumn(col)
    printRanking(ranking)

def printRanking(ranking):
    numberResults = optionBannerNumberResults()
    for index, dado in enumerate(ranking[:numberResults]):
        print('{} - {} : {} notebooks'.format(index+1, dado[0], dado[1]))

def choosecolumn(colunas):
    while True:
        try:
            choice = int(input("Escolha a coluna > "))
            return colunas[choice - 1]
        except KeyboardInterrupt:
            return
        except:
            print("ERRO: Por favor entre com uma opção válida")
def optionBannerNumberResults():
        while True:
            try:
                return int(input("Número de resultados a exibir > "))
            except KeyboardInterrupt:
                return
            except:
                print("Digite uma entrada válida")

def optionBanner(colunas):
    print('Escolha por qual coluna você quer ver os resultados\n')

    for index, coluna in enumerate(colunas):
        print('[{}] - {}'.format(index + 1, coluna))

if __name__ == '__main__':
    main()
