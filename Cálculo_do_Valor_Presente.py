def vp(vf, r, n):
    x = vf / (1 + r) ** n
    return x

valor_futuro=float(input("Informe o valor futuro: "))
juros=float(input("Informe a taxa de juros: "))
tempo=float(input("Informe o tempo: "))

valor_presente=vp(valor_futuro,juros,tempo)
print('valor Futuro = ', valor_futuro )
print('Valor Presente = ', valor_presente)
