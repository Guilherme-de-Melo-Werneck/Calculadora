import math #para usar funções matemáticas, como raiz quadrada, logaritmo, seno, cosseno, etc

def soma(a, b): #a função soma que recebe dois argumentos a e b e retorna a soma dos dois valores.
    return a + b

def subtracao(a, b): #função subtracao que recebe dois argumentos a e b e retorna a diferença entre eles.
    return a - b

def multiplicacao(a, b): #função multiplicacao que recebe dois argumentos a e b e retorna o produto dos dois valores.
    return a * b

def divisao(a, b): #divisao que recebe dois argumentos a e b e retorna a divisão de a por b. Verifica se b é diferente de zero para evitar uma divisão por zero
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def raiz_quadrada(a): #função raiz_quadrada que recebe um argumento a e retorna a raiz quadrada de a.
    return math.sqrt(a)

def potenciacao(a, b): #função potenciacao que recebe dois argumentos a e b e retorna a elevado à potência b usando o operador **.
    return a ** b

def resto_divisao(a, b): #função resto_divisao que recebe dois argumentos a e b e retorna o resto da divisão de a por b usando o operador %.
    return a % b

def fatorial(a): #função fatorial que recebe um argumento a e retorna o fatorial de a.
    return math.factorial(a)

def logaritmo(a, b): #função logaritmo que recebe dois argumentos a e b e retorna o logaritmo de a na base b.
    return math.log(a, b)

def seno(angulo): #função seno que recebe um argumento angulo em graus e retorna o seno do ângulo.
    return math.sin(math.radians(angulo))

def cosseno(angulo):  # função cosseno que recebe um argumento angulo em graus e retorna o cosseno do ângulo
    return math.cos(math.radians(angulo))

def tangente(angulo):  # função tangente que recebe um argumento angulo em graus e retorna a tangente do ângulo
    return math.tan(math.radians(angulo))

print("Selecione a operação:") #imprime o menu de opções para o usuário escolher a operação matemática desejada
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Raiz Quadrada")
print("6. Potenciação")
print("7. Resto da Divisão")
print("8. Fatorial")
print("9. Logaritmo")
print("10. Seno")
print("11. Cosseno")
print("12. Tangente")

escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8/9/10/11/12): ") #Solicita ao usuário que digite a escolha da operação.

if escolha in ['1', '2', '3', '4']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(num1, "+", num2, "=", soma(num1, num2))

    elif escolha == '2':
        print(num1, "-", num2, "=", subtracao(num1, num2))

    elif escolha == '3':
        print(num1, "*", num2, "=", multiplicacao(num1, num2))

    elif escolha == '4':
        print(num1, "/", num2, "=", divisao(num1, num2))

elif escolha in ['5', '6']:
    num = float(input("Digite o número: "))

    if escolha == '5':
        print("Raiz quadrada de", num, "=", raiz_quadrada(num))
        
    elif escolha == '6':
        exp = float(input("Digite o expoente: "))
        print(num, "elevado a", exp, "=", potenciacao(num, exp))

elif escolha == '7':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Resto da divisão de", num1, "por", num2, "=", resto_divisao(num1, num2))

elif escolha == '8':
    num = int(input("Digite o número: "))
    print("Fatorial de", num, "=", fatorial(num))

elif escolha == '9':
    num = float(input("Digite o número: "))
    base = float(input("Digite a base do logaritmo: "))
    print("Logaritmo de", num, "na base", base, "=", logaritmo(num, base))

elif escolha == '10':
    angulo = float(input("Digite o ângulo em graus: "))
    print("Seno de", angulo, "=", seno(angulo))

elif escolha == '11':
    angulo = float(input("Digite o ângulo em graus: "))
    print("Cosseno de", angulo, "=", cosseno(angulo))

elif escolha == '12':
    angulo = float(input("Digite o ângulo em graus: "))
    print("Tangente de", angulo, "=", tangente(angulo))

else:
    print("Opção inválida.")