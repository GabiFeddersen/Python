
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau 1"
    elif imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

# Calcular IMC
imc = calcular_imc(peso, altura)
    
# Interpretar o IMC
interpretacao = interpretar_imc(imc)
    
# Exibir o resultado
print(f"Seu IMC é {imc:.2f}. Você está classificado como: {interpretacao}")
