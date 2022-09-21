# Creacion lista_menu
# el primer item cargar "vacio"
# por compatibilidad con otras listas
import pickle
cantidad_items = int(input('ingrese cantidad de items: '))


def creacion_menu(cantidad_items):

    lista_menu = []
    lista_precio = []

    for i in range(cantidad_items):
        menu = input('ingrese menu: ')
        lista_menu.append(menu)
        precio = float(input('ingrese precio: '))
        lista_precio.append(precio)

    return lista_menu, lista_precio


lista_menus, lista_precios = creacion_menu(cantidad_items)

indice = 0
print('este es el listado de precios')

for i in lista_menus:

    print(indice, end='\t')
    print(lista_menus[indice], end='\t')
    print('$', lista_precios[indice])
    indice = 1 + indice


archivo_menus = open('lista_menu', 'wb')
pickle.dump(lista_menus, archivo_menus)
archivo_menus.close()

archivo_precios = open('lista_precio', 'wb')
pickle.dump(lista_precios, archivo_precios)
archivo_precios.close()

