import clase

a = float(input("Ingrese un valor para el area del cuadrado: "))
b = float(input("Ingrese valor b para operar: "))
c = float(input("Ingrese valor c para operar: "))


object1 = clase.Square(c)
print(f"From class Square: {object1.getVal()}")

# Crear objeto para la clase Add_Sub
object2 = clase.Add_Sub()

print(f"From class Add_Sub: Suma {object2.add(b, c)}")
print(f"From class Add_Sub: Resta {object2.sub(b, c)}")
print(f"From class Add_Sub: Multiplicacion {object2.mul(b, c)}")
print(f"From class Add_Sub: Division {object2.div(b, c)}")

