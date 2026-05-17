print("CALCULADORA DE PROMEDIO DE NOTAS")

nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("Tu promedio es:", promedio)

if promedio >= 51:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")