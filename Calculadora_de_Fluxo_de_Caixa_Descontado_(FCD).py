# Definição da Função
def fcd(taxa, ano1, ano2, ano3):

    vp1 = ano1 / (1 + taxa)
    vp2 = ano2 / ((1 + taxa) ** 2)
    vp3 = ano3 / ((1 + taxa) ** 3)

    valor_total = vp1 + vp2 + vp3

    return(valor_total)

# Código principal
a = float(input("Digite a taxa: "))
b = float(input("Fluxo de caixa Primeiro ano: "))
c = float(input("Fluxo de caixa Segundo ano: "))
d = float(input("Fluxo de caixa Terceiro ano: "))

print(fcd(a, b, c, d))
