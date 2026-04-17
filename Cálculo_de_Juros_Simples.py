import matplotlib.pyplot as plt
import numpy as np

c = float(input("capital: "))
r = float(input("taxa de juros: "))
t_total = int(input("Digite o tempo total (em meses): "))

# vetor de tempo (0 até t_total)
t = np.arange(0, t_total + 1)

# fórmula correta do montante (juros simples)
montantes = c * (1 + r * t)

print (t)
print(montantes)

# gráfico
plt.plot(t, montantes)
plt.xlabel("Tempo (anos)")
plt.ylabel("Montante")
plt.title("Juros Simples")
plt.grid()

plt.show()
