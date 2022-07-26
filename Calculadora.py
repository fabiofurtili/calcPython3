print("Calculadora - Python3")
#Operadores
def somar(a, b):
    return(a + b)
def subtrair(a, b):
    return(a - b)
def multiplicar(a, b):
    return(a * b)
def dividir(a, b):
    return(a / b)

#Entrada de dados
primeiroValor = int(input("Primeiro valor: "))
operador = input("Escolha o operador: ")
segundoValor = int(input("Segundo valor: "))

#Saida de dados
print(f"{primeiroValor} {operador} {segundoValor} =")
if operador == "+":
    print(somar(primeiroValor, segundoValor))
elif operador == "-":
    print(subtrair(primeiroValor, segundoValor))
elif operador == "*":
    print(multiplicar(primeiroValor, segundoValor))
elif operador == "/":
    print(dividir(primeiroValor, segundoValor))
else:
    print("Informações incorreta!")
