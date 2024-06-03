listaProduto = [] 
 
print('Bem-vindo ao Controle de Estoque da mercearia de Leonardo Vitorio') 
 
 
def cadastrarProduto(codigo): 
 
  print('Você selecionou a opção de Cadastrar Produto') 
  print('O código da Produto é: {:0>3}'.format(codigo)) 
  nome = input('Entre com o nome da Produto:') 
  fabricante = input('Entre com o fabricante da Produto:') 
  valor = float(input('Entre com o valor R$ da Produto:')) 
  dicionarioProduto = {'codigo'   : codigo, 
                         'nome' : nome, 
                         'fabricante': fabricante, 
                         'valor': valor} 
  listaProduto.append(dicionarioProduto.copy()) 
 
def consultarProduto(): 
 
  while True: 
 
    try: 
      print('Você Selecionou a Opção de Consultar Produto') 
      opConsultar = int(input('Entre com a opção desejada\n1- Consultar Todas as Produto\n2- Consultar Produto por Código\n3- Consultar Produto por Fabricante\n4- Retornar\n-->')) 
 
      if opConsultar == 1: 
        print('-' * 20) 
 
        for pecas in listaProduto: 
 
            for key, value in pecas.items(): 
              print('{} : {}'.format(key,value)) 
            print('-' * 20) 
 
      elif opConsultar == 2: 
        print('Você Selecionou a Opção Produto por Código') 
        entrada = int(input('Digite o Código: ')) 
        print('-' * 20) 
 
        for Produto in listaProduto: 
 
          if(Produto['codigo'] == entrada): 
 
            for key, value in Produto.items(): 
              print('{} : {}'.format(key,value)) 
            print('-' * 20) 
 
      elif opConsultar == 3: 
        print('Você Selecionou a Opção Produto por Fabricante') 
        entrada = input('Digite o Fabricante: ') 
        print('-' * 20) 
 
        for Produto in listaProduto: 
 
          if(Produto['fabricante'] == entrada): 
 
            for key, value in Produto.items(): 
              print('{} : {}'.format(key,value)) 
            print('-' * 20) 
 
      elif opConsultar == 4: 
        break 
 
      else: 
        print('Por favor digite somente o que pede') 
        continue 
 
    except ValueError: 
      print('Por Favor pare de digitar números que não existe...') 
      continue 
 
def removerProduto(): 
 
    print('Você Selecionou o Remover Produto') 
    entrada = int(input('Digite o Código da Produto que irá remover: ')) 
 
    for Produto in listaProduto: 
 
      if(Produto['codigo'] == entrada): 
        listaProduto.remove(Produto) 
 
    else: 
      print('Você removeu o código.') 
 
registroProduto = 0 
while True: 
 
    try: 
      opcao = int(input('Digite a opção desejada:\n1- Cadastrar Produto\n2- Consultar Produto\n3- Remover Produto\n4- Sair\n-->')) 
      if opcao == 1: 
        registroProduto = registroProduto + 1 
        cadastrarProduto(registroProduto) 
 
      elif opcao == 2: 
        consultarProduto() 
 
      elif opcao == 3: 
        removerProduto() 
 
      elif opcao == 4: 
        print('Programa finalizado') 
        break 
 
      else: 
        print('Digite somente uma das opções do MENU') 
        continue 
 
    except ValueError: 
        print('Pare de digitar números que não existe...') 