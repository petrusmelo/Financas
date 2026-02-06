def vp(vf,r,n):
  x=vf/(1+r)**n
  return(x)

valor_futuro=float(input("Informe o valor futuro: "))
juros=float(input("Informe a taxa de juros: "))

valor_presente=vp(valor_futuro,juros,1)

print('valor Futuro = ', valor_futuro )
print('Valor Presente = ', valor_presente)
