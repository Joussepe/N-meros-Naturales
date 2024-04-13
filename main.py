class CalculadoraMCD:
    def calcular_mcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamar al método calcular_mcd de la instancia de la clase CalculadoraMCD
mcd = calculadora.calcular_mcd(num1, num2)

# Imprimir el resultado
print("El máximo común divisor de", num1, "y", num2, "es:", mcd)