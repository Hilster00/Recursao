def mochila(capacidade,items):
    #items[item_0,item_1...item_n]
    #item_n[valor,massa]
  
    if capacidade < 1:
        return 0
      
    #ordena pela massa do item
    items=sorted(items,key=lambda i:i[1])
    valores=[]

    for item in items:
        #verifica se ainda não ultrapassou a capacidade
        if item[1] > capacidade:
            break

        #pega o item 'n' e se chama recursivamente
        filho=item[0]+mochila(capacidade-i[1],items)
      
        #guarda a melhor recursão obtida pelo filho
        valores.append(filho)

    return max(valores)
    
print(mochila(15,[[1,1],[10,2]]))
