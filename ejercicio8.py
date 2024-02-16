numeros = [int(input("Introduce el número {}: ".format(i+1))) for i in range(5)]
suma_total = sum(numeros)
num_impares = len([num for num in numeros if num % 2 != 0])
hay_mayor_100 = any(num > 100 for num in numeros)
print("Suma total:", suma_total)
print("Cantidad de números impares:", num_impares)
print("¿Existen números superiores a 100?", "Sí" if hay_mayor_100 else "No")
