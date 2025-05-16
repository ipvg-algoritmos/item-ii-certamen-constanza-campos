# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código
# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código
cantidad_notas = int(input("¿Cuántas notas deseas ingresar? "))
notas = []

for i in range(cantidad_notas):
    while True:
            nota = float(input(f"Ingresa nota {i+1} (1.0-7.0): "))
            if 1.0 <= nota <= 7.0:
                notas.append(nota)
                break
            print("Error: Ingresa un valor numérico válido")

if cantidad_notas > 0:
    resultado = sum(notas) / cantidad_notas
    resultado = round(resultado, 2)
    print(f"Promedio: {resultado}")
    if resultado >= 4.0:
        print("Has aprobado")
    else:
        print("Has reprobado")
else:
    print("No se ingresaron notas para calcular el promedio")