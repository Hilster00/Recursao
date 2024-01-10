# Função para calcular o MDC usando o algoritmo de Euclides
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Função para calcular o MMC usando o MDC
def mmc(a, b):
    return (a * b) // mdc(a, b)

# Teste da função com dois números inteiros positivos
num1 = 12
num2 = 18
resultado = mmc(num1, num2)
print(f"O MMC de {num1} e {num2} é: {resultado}")
