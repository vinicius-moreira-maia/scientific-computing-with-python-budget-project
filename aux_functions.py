from math import floor

def round_down(x):
  '''
  Retorna o número arredondado para o menor múltiplo de 10 antes dele.
  '''
  
  if x < 10:
    return 0
  else:
    return x // 10 * 10

def get_percentages(categories):
  '''
  Recebe a lista dos objetos e retorna uma lista de dicionários com a porcentagem gasta para cada categoria (arredondada para o 'menor 10 / lowest 10').
  '''
  gastos = []
  num_gastos = 0
  for cat in categories:
    for dicio in cat.ledger:
      if dicio['amount'] < 0:
        num_gastos += dicio['amount']

    # calculando a porcentagem apenas a partir do depósito inicial (se houver), e não dos outros depósitos
    porc = 0
    if cat.ledger[0]['description'] == 'initial deposit':
        porc = (num_gastos * -1 / cat.ledger[0]['amount']) * 100
        gastos.append({'categoria': cat.category, 'porcentagem_gasta': round_down(floor(porc))})
    else:
      gastos.append({'categoria': cat.category, 'porcentagem_gasta': round_down(floor(porc))})
    num_gastos = 0

  # print(gastos) (depuração)
  return gastos

def build_bars(gastos):
  '''
  Recebe a lista de dicionários contendo os nomes das categorias e as porcentagens gastas e retorna o gráfico de barras preenchido.
  '''
  
  # template das barras
  porcentagens = []
  for i in range(11):
    if len(str(i*10)) == 1:
       porcentagens.append(['  ', str(i*10), '| '])
    elif len(str(i*10)) == 2:
       porcentagens.append([' ', str(i*10), '| '])
    else:
       porcentagens.append([str(i*10), '| '])

  # preenchendo o gráfico
  for i in range(11):
    for gasto in gastos:
      if gasto['porcentagem_gasta'] >= i * 10:
        porcentagens[i].append('o')
        porcentagens[i].append('  ')
      else:
        porcentagens[i].append('   ')

  # barra de '-'
  tam = len(porcentagens[0])
  porcentagens.insert(0, ['    ', (tam + 1) * '-'])

  # print(porcentagens) (depuração)
  return porcentagens
  
def get_category_names(categories):
  '''
  Retorna os nomes de cada cadegoria formatados para exibição no terminal.
  '''
  
  # achando o maior nome de categoria entre os objetos
  maior = ''
  for cat in categories:
    if len(cat.category) > len(maior):
      maior = cat.category

  l = []
  l2 = []
  for i in range(len(maior)):
    l2.append(' ' * 5)
    for cat in categories:
      try:
        l2.append(cat.category[i] + '  ')
      except:
        l2.append(' ' + '  ')
    l2.append('\n')
    l.append(l2)
    
  # print(l) (depuração) -> a lista não está correta (repete os nomes das categorias)

  # desmembrando a lista de listas 'l' em uma lista só de caracteres 'l3'
  l3 = []
  for q in l:
    for i in range(len(q)):
      l3.append(q[i])

  # correção do bug da lista 'l', mas sei que deveria ser corrigido lá
  dif = len(''.join(l3)) // len(maior)

  # print(l3[:dif]) (depuração)

  return ''.join(l3)[:dif]

def show_bars_and_category_names(nomes, porcentagens):
  '''
  Retorna uma string com a junção dos nomes e das porcentagens pronta para ser exibida no terminal.
  '''
  
  porcentagens.reverse()
  
  porcentagens.append(nomes)
  
  result = 'Percentage spent by category\n'
  for i in porcentagens:
    result += ''.join(i)
    result += '\n'

  # remoção de 2 linhas em branco que passaram despercebidas
  result = result[:len(result) - 2]

  return result