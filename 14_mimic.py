
"""
14. mimic
Neste desafio você vai fazer um gerador de lero-lero.
É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.
Para isso você precisa:
A. Abrir o arquivo especificado via linha de comando.
B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.
C. Criar um dicionário de "imitação".
Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.
Por exemplo, suponha um arquivo com o conteúdo: A B C B A
O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B
Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.
Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.
Use a string vazia como a primeira palavra do texto para preparar as coisas.
Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""
from collections import defaultdict
from random import choice
import sys


def list_create(filename):
  arq = open(filename)
  list_1 = []
  for i in arq.readlines():
    list_1.extend(i.split())
  arq.close()
  return list_1


def gera_tuplas(lista):
  s = []
  for i in range((len(lista) - 1)):
    a ,b = lista[i], lista[ i +1]
    s.append((a ,b))
  return s


def mimic_dict(filename):
  """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes.
  """
  lista = list_create(filename)
  tuplas = gera_tuplas(lista)
  d = defaultdict(list)
  for k, v in tuplas:
    d[k].append(v)
  d[''].append(lista[0]) # chave '' contém uma lista com a primeira palavra
  d[lista[-1]].append('') # última palavra contém uma lista com a palavra ''
  sorted(d.items())
  return d


def print_mimic(mimic_dict, word):
  """Dado o dicionario imitador e a palavra inicial,
  imprime texto de 200 palavras.
  Entrada: dict, palavra inicial
  Saída: text 200 palavras
  """
  i = 0
  while i < 200:
    lista = mimic_dict[word]
    palavra = choice(lista)
    print(word, end = ' ')
    word = palavra
    i += 1


def main():
  if len(sys.argv) != 2:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
