class Ropa:
    def __init__(self, color='rojo', talla='S', estilo='camisa', precio=0):
        self.color=color
        self.talla=talla
        self.estilo=estilo
        self.precio=precio
        
    def cambiar_precio(self, precio):
        self.precio=precio
        
    def cambiar_talla(self, talla):
        self.talla=talla


ropa_mujer = Ropa(estilo='falda', precio=10, talla='S', color='azul')
print(ropa_mujer.color)

print(ropa_mujer.precio)

ropa_mujer.cambiar_precio(1)
print(ropa_mujer.precio)

ropa_hombre = Ropa('verde', 'XL', 'pantalon', 20)
print(ropa_hombre.talla)

ropa_hombre.cambiar_talla('M')
print(ropa_hombre.talla)

cliente = Ropa()
print(cliente.talla, cliente.precio, cliente.estilo)

import Class.pow2 as num

val = num.Pow2(3)

print(val.pow2())
print(val.mod2())
print(val.pow3())





