usuario = input("Ingresa tu Nombre Aqui: ")


print("""
Bienvenidos a la Calculadora Mental
""", usuario.strip().capitalize())

print("Para Comenzar Debes Escoger Dos Numeros Al Azar")

n1 = input("INGRESA TU PRIMER NUMERO: ")
n2 = input("INGRESA TU SEGUNDO NUMERO: ")

n1 = int(n1)
n2 = int(n2)


print("Genial", usuario.strip().capitalize(), """Lo haz hecho bien,
    has escogido los numeros:""", n1, "y", n2, """
    Ahora, Debes Seleccionar Que Tipo de Operacion Deseas
    Realizar. Bien Sea Suma(SUM),Resta(RES),Multiplicacion(MUL) y Division(DIV).
    """)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2


tipo_operacion = input("""Ingresa el tipo de Operacion
                       suma - suma
                       resta - resta
                       multi - multiplicacion
                       divi - division
                       
                       """)

print("Vamos a Hacer un Orden de Todos Los Datos Que Tenemos de Ti.")


print("Nombre: ", usuario.strip().capitalize())
print("Numeros: ", n1, "y", n2)
print("Tipo de Operacion: ", tipo_operacion)


mensaje_sum = f"Operacion Igual a:{suma}"
mensaje_res = f"Operacion Igual a:{resta}"
mensaje_mul = f"Operacion Igual a:{multi}"
mensaje_div = f"Operacion Igual a:{divi}"


while tipo_operacion.lower() == "suma":
    print(mensaje_sum)

while tipo_operacion.lower() == "resta":
    print(mensaje_res)
    break

while tipo_operacion.lower() == "multi":
    print(mensaje_mul)
    break

while tipo_operacion.lower() == "divi":
    print(mensaje_div)
    break

while tipo_operacion.lower() != "suma" or "resta" or "multi" or "divi":
    print("Error, Palabra Incorrecta, Reinicie Codigo. BIp Bip")
    break

print("""
FELICITACIONES, HAS TERMINADO EL JUEGO
      ERES INCREIBLE!!!!""", usuario, "!!")

# No he podido Recordar Como Puedo Hacer para Evitar un error
# en un Mensaje
