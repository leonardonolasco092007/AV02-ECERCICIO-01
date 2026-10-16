#Q1:
try:
    nm1 = float(input("Digite o primeiro número: "))
    nm2 = float(input("Digite o segundo número: "))

    resultado = nm1 / nm2

except ValueError:
    print("Entrada inválida! Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero!")

else:
    print("Resultado:", resultado)


#Q2:
def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media


resultado = calcular_media([8, 7, 9, 6])
print(resultado)


#Q3:
def verificar_carga(horas):
    if horas >= 40:
        return "Carga completa"
    else:
        return "Carga incompleta"


print(verificar_carga(40))
print(verificar_carga(35))


#Q4:
def calcular_saldo(saldo, valor, operacao):
    if operacao == "Deposito":
        return saldo + valor

    elif operacao == "Saque":
        return saldo - valor

    else:
        return "Operação inválida"


print(calcular_saldo(1000, 200, "Deposito"))
print(calcular_saldo(1000, 200, "Saque"))


#Q5:
def filtrar_aprovados(notas):
    aprovados = []

    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)

    return aprovados


resultado = filtrar_aprovados([5, 7, 8.5, 6, 10, 4])
print(resultado)




