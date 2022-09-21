import pickle

archivo_menus = open('lista_menu', 'rb')
lista_menus = pickle.load(archivo_menus)
archivo_menus.close()

archivo_precios = open('lista_precio', 'rb')
lista_precios = pickle.load(archivo_precios)
archivo_precios.close()

hacer_pedido = input('hacer_pedido?')


def creacion_pedido(hacer_pedido):

    lista_cantidad_pedido = []
    lista_item_pedido = []
    lista_item_precio = []

    item_pedido = 1

    while item_pedido > 0:
        item_pedido = int(input('ingrese item_pedido: '))
        if item_pedido == 0:
            print('fin')
            break
        else:
            lista_item_pedido.append(item_pedido)
            cantidad_pedido = int(input('ingrese cantidad_pedido: '))
            lista_cantidad_pedido.append(cantidad_pedido)
            lista_item_precio.append(
                lista_precios[item_pedido])

    return lista_cantidad_pedido, lista_item_pedido, lista_item_precio


lista_cantidad_pedido, lista_item_pedido, lista_item_precio = creacion_pedido(
    hacer_pedido)

indice = 0
print('este es el listado de pedidos')
total = 0
for i in lista_cantidad_pedido:

    print(indice, end='\t')
    print(lista_cantidad_pedido[indice], end='\t')
    print(lista_menus[lista_item_pedido[indice]], end='\t')
    print('c/u $', lista_item_precio[indice], end='\t')
    print('$', lista_cantidad_pedido[indice]*lista_item_precio[indice])
    total = total+lista_cantidad_pedido[indice]*lista_item_precio[indice]
    indice = 1 + indice

print('\t \t \t \t total $', total)


archivo_pedido = open('lista_cantidad_pedido', 'wb')
pickle.dump(lista_cantidad_pedido, archivo_pedido)
archivo_pedido.close()

archivo_precios = open('lista_item_precio', 'wb')
pickle.dump(lista_item_precio, archivo_precios)
archivo_precios.close()

archivo_cantidad_pedido = open('lista_cantidad_pedido', 'wb')
pickle.dump(lista_cantidad_pedido, archivo_cantidad_pedido)
archivo_cantidad_pedido.close()


archivo_item_pedido = open('lista_item_pedido', 'wb')
pickle.dump(lista_item_pedido, archivo_item_pedido)
archivo_item_pedido.close()

archivo_item_precio = open('lista_item_precio', 'wb')
pickle.dump(lista_item_precio, archivo_item_precio)
archivo_item_precio.close()
