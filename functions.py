def return_hello():
    return 'Hello'

variable = return_hello()
print(variable)


####################################


def inverse(lista):#inverter lista
    lista.reverse()
    return lista

lista_invertida = inverse([1, 2, 3])
print(lista_invertida)