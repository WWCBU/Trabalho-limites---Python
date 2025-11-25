# --------------------------
# MODELO REAL: DESCRARGA DE UM CAPACITOR
# V(t) = V0 * e^(-t / (R*C))
# --------------------------

# Parâmetros reais do circuito


#Importação de bibliotecas

import numpy as np
import matplotlib.pyplot as plt

#Funções auxiliares


#Função principal do programa
def main():



#Executa a função principal
main()





# Constante de tempo tau = RC
tau = R * C

print(f"Constante de tempo do circuito (tau): {tau} segundos")

# Criando vetores de tempo
t = np.linspace(0, 0.01, 300)  # 0 a 0.01 segundos

# Função da tensão durante a descarga
V = V0 * np.exp(-t / tau)

# Mostrando valores iniciais e finais
print(f"Tensão inicial: {V[0]:.2f} V")
print(f"Tensão após 0.01 s: {V[-1]:.4f} V")

# Limite quando t → infinito
V_limite = 0
print(f"Limite da tensão quando t tende ao infinito: {V_limite} V")

# --------------------------
# GRÁFICO
# --------------------------

plt.plot(t, V, label="V(t) = V0 * exp(-t/RC)")
plt.title("Descarga de um Capacitor RC")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.legend()
plt.show()
