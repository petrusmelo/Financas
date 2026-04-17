import matplotlib.pyplot as plt
import numpy as np

c = float(input("capital: "))
r = float(input("taxa de juros: "))
t_total = int(input("Digite o tempo total (em meses): "))

t = np.arange(0, t_total + 1)

montante = c * ((1 + r)**t)

print (t)
print(montante)

# gráfico
plt.plot(t, montante)
plt.xlabel("Tempo (meses)")
plt.ylabel("Montante")
plt.title("Juros Compostos")
plt.grid()

plt.show()
