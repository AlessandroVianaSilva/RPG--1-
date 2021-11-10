mapa = {

  'sala':{
    'leste':'sala de jantar',
  },
  'sala de jantar':{
    'oeste':'sala',
    'sul': 'quarto',
    'leste':'cozinha',
    'itens': 'armadura'
  },
  'quarto':{
    'norte': 'sala de jantar',
    'itens': 'espada'
  },
   'cozinha':{
    'oeste': 'sala de jantar',
    'sul': 'quintal',
    'itens':'Ogro',
    
  },
  'quintal':{
    'norte':'cozinha',
    'leste': 'fora da casa',
    'itens': 'feitiço'
  },
  'fora da casa':{
    'oeste': 'quintal'
  }
}

inventario = []
mensagem_inicial = '''
Demo - Jogo RPG
============
Olá jovem aventureiro! 
Pronto para sua primeira missão?
Aqui vamos nós
Seu Objetivo -> Pegar os Equipamentos que está na casa e sair

Equipamentos: Espada e Armadura

Fique atento!
=============================================================
Comandos:
para [direcao] - 
norte 
sul,
leste 
ou oeste
pegar [item]
============
'''
local_atual = 'sala'
def mostra_status(local,inventario,mapa):
  print('------------------')
  print('Seu local atual:',local)
  if 'itens' in mapa[local]:
    print('eu estou vendo o item:',mapa[local]['itens'])
  print('inventario',inventario)
  print('------------------')
print(mensagem_inicial)
while True:
  mostra_status(local_atual,inventario,mapa)
  comando = input('> ').lower().split(' ')
  if comando[0] == 'para':
    direcao = comando[1]
    if direcao in mapa[local_atual]:
      local_atual = mapa[local_atual][direcao]
      if 'itens' in mapa[local_atual]:
        if 'Ogro' in mapa[local_atual]['itens']:
          print('no local',local_atual,'existe um Ogro')
          inventario.append('Ogro')
    else:
      print('Não é possível ir para essa direcao')
  elif comando[0] == 'pegar':
    item = comando[1]
    if item in mapa[local_atual]['itens']:
      inventario.append(item)
      del mapa[local_atual]['itens']
      print(item, 'agora é seu')
    else:
      print('Não tem esse item nesse local')
  else:
    print('comando inválido')
  
  if 'Ogro' in inventario and 'espada'not in inventario and 'armadura' not in inventario:
    print('--------------------------------------------------')
    print('Voce foi morto por nao estar equipado o suficiente')
    print('GAME OVER')
    break
  
  elif 'Ogro'in inventario and 'espada' in inventario and 'armadura' in inventario:
    print('Voce matou o inimigo e segue adiante na jornada')
    inventario.remove('Ogro')
    del mapa[local_atual]['itens']
  
  if local_atual == 'fora da casa' and 'espada' in inventario and 'armadura' in inventario and 'feitiço' in inventario:
    print('''
    -----------------------------------------------------------
    Parabéns! 
    Você obteve sucesso em sua primeira missão!
    Coletou os equipamentos necessarios para matar o inimigo
    e pegou um Feitiço raro que será importante em sua jornada!
    ''')
    break