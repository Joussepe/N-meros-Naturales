class CalculadoraMCD:
    def calcular_mcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def calcular_mcm(self, num1, num2):
        mcd = self.calcular_mcd(num1, num2)
        mcm = (num1 * num2) // mcd
        return mcm


# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular el MCD y el MCM utilizando la instancia de la clase CalculadoraMCD
mcd = calculadora.calcular_mcd(num1, num2)
mcm = calculadora.calcular_mcm(num1, num2)

# Imprimir los resultados
print("El máximo común divisor de", num1, "y", num2, "es:", mcd)
print("El mínimo común múltiplo de", num1, "y", num2, "es:", mcm)