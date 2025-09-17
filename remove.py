caixão = []
opcao = 0
while opcao != 6:
    opcao = int(input("Escolha oq deseja fazer: \n 1- Ver caixão \n 2-Adicionar item no caixão \n 3- Remover itens no caixão \n 4-Modificar caixão \n 5-Limpando caixão\n 6-Sair \n"))
    if opcao == 1:
        print(f"Itens na mochila  : \n {caixão}")
    elif opcao == 2:
        item = input(f"Digite o nome do item a ser adicionado: \n {caixão}")
        caixão.append(item)
    elif opcao ==3:
        item = input("Digite o que vc quer remover do caixão: \n")
        caixão.remove(item)
    elif opcao == 4:
        item = input("oq vc quer modificar:")
        caixão.index(item)
    elif opcao == 5:
        print("limpando caixão")
        caixão.clear(item)
else:
    print("Sair")
