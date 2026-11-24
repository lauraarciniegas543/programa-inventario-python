
# Programa de control de inventario y reabastecimiento
# Problema 3 - Fase 5

# Matriz con los datos de cinco articulos
inventario = [
    [ "001", "Arroz", 8, 20 ],
    [ "002", "Aceite", 15, 10 ],
    [ "003", "Leche", 4, 12 ],
    [ "004", "Azucar", 10, 10 ],
    [ "005", "Pasta", 6, 15 ]
]

# Funcion para calcular la cantidad a solicitar
def calcular_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir


# Mostrar los resultados del inventario
print("======================================")
print("   CONTROL DE INVENTARIO")
print("======================================")
print("Articulo          Cantidad a solicitar")
print("--------------------------------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_reabastecimiento(
        stock_actual, stock_minimo
    )

    print(nombre, "          ", cantidad, "unidades")

print("--------------------------------------")
print("Total de unidades a solicitar:")

total = 0

for articulo in inventario:
    total += calcular_reabastecimiento(articulo[2], articulo[3])

print(total, "unidades")
print("======================================")
print("Fin del programa")
