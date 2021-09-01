def precio_sin_descuento(tipo_silla,cantidad):
  precio_base=0 #no es necesario, sólo es una buena práctica
  if (tipo_silla=="1"):
    precio_base=700
  elif (tipo_silla=="2"):
    precio_base=900
  else:
    precio_base=1500
  return precio_base*cantidad
  
def calcular_descuento(tipo_cliente,precio_base):
  if(tipo_cliente=="1"):
    if(precio_base>=10000 and precio_base<20000):
      return precio_base*.10
    elif (precio_base>20000):
      return precio_base*.15
    else:
      return 2
  if(tipo_cliente=="2"):
    return precio_base*.20

def calcular_total(subtotal,descuento):
  return subtotal-descuento

tipo_cliente=input("Cuál es el tipo de cliente? \n 1) Normal \n 2) Frecuente \n")
tipo_silla=input("Cuál es el tipo de silla? \n 1) Básica \n 2) Estándar \n 3) De lujo \n")
cantidad_a_comprar=int(input("Cuál es la cantidad de sillas a comprar? \n"))

subtotal=precio_sin_descuento(tipo_silla,cantidad_a_comprar)
descuento=calcular_descuento(tipo_cliente,subtotal)
total=calcular_total(subtotal,descuento)

print("Precio antes del descuento: $"+str(subtotal))
print("Descuento: $"+str(descuento))
print("Precio total: $" +str(total))