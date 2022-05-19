def total():
    pass
# add_product = input('ingresa los productos: ')

inventario = ['azúcar', 'sal', 'huevos', 'tomate', 'carne', 'pollo']
valor = [2200, 1000, 600, 3000, 7000, 6000]
carrito = []

menu = f'''
Hola usuario, bienvenido al sistema de venta

por favor seleccione el ID del producto
1.{inventario[0]}
2.{inventario[1]}
3.{inventario[2]}
4.{inventario[3]}
5.{inventario[4]}
6.{inventario[5]}

presiona "Ctrl + C" pra finalizar

'''
print(menu)

try:
    while True:
        # inventario.append(input('ingresa los productos: ')) #para agregar nuevos productos
        # valor.append(input('Ingresa el valor del producto: ')) #para agregar nuevos valores
        # inventario_2 = (input('ingresa el producto: ')(input('ingresa el valor: ')) ) # esta linea era para agregar los productos y los valores a un diccionario (pero así no se hace y no funcionó)
        carrito.append(int(input('Ingresa el ID del producto: ')))
except KeyboardInterrupt:
    pass

print('')
print('Tu valor a pagar es: ')

for i in (carrito):
    print(valor[i-1])

