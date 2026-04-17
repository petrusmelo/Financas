import yfinance as yf
import matplotlib.pyplot as plt

ticker = "PETR4.SA"

acoes = yf.download(ticker, period="1mo")

print(acoes)

plt.plot(acoes["Close"], label = "PETR4")
plt.xlabel("Data")
plt.ylabel("Preço (R$)")
plt.show()
