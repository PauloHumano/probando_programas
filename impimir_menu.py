import pickle

archivo_menus = open('lista_menu', 'rb')
lista_menus = pickle.load(archivo_menus)
print(lista_menus)
archivo_menus.close()

archivo_precios = open('lista_precio', 'rb')
lista_precios = pickle.load(archivo_precios)
print(lista_precios)
archivo_precios.close()

indice = 0
print('este es el listado de precios')

for i in lista_menus:

    print(indice, end='\t')
    print(lista_menus[indice], end='\t')
    print('$', lista_precios[indice])
    indice = 1 + indice
