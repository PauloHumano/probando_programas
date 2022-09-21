
nombres = []
cuenta = int(0)
cuenta_correa = int(0)
cuenta_perros = int(0)
cuenta_gatos = int(0)


def agrega_mascota(self):
    global nombres
    global cuenta
    global cuenta_correa
    global cuenta_perros
    global cuenta_gatos
    nombres.append(self.nombre)
    cuenta = len(nombres)
    if self.correa:
        cuenta_correa += 1
    else:
        pass
    if self.raza == "perro":
        cuenta_perros += 1
    elif self.raza == "gato":
        cuenta_gatos += 1
    else:
        pass

    if len(nombres) == 1:
        print("en el salon esta ", nombres)
    else:
        if cuenta_correa == cuenta or cuenta == cuenta_gatos or cuenta == cuenta_perros:
            print("en el salon estan jugando\n", nombres)
        else:
            print("en el salon estan peleando\n", nombres)


class Mascota:

    def __init__(self, raza, nombre, correa):

        self.raza = raza
        self.nombre = nombre
        self.correa = bool(correa)

        agrega_mascota(self)


mascota = Mascota("gato", "cleo", True)
mascota2 = Mascota("gato", "frodo", True)
mascota3 = Mascota("perro", "manchita", True)
mascota4 = Mascota("perro", "apolo", False)


print("cantidad de perros=", cuenta_perros)
print("cantidad de gatos=", cuenta_gatos)
