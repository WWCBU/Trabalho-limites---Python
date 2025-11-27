# --------------------------
# MODELO REAL: DESCARGA DE UM CAPACITOR
# V(t) = V0 * e^(-t / (R*C))
# --------------------------

import numpy as np
import matplotlib.pyplot as plt

def main():

    # ----- Entrada de dados do usuário -----
    V0 = float(input("Digite a tensão inicial do capacitor (V0) em Volts: "))
    V_alvo = float(input("Digite a tensão alvo desejada (Volts): "))

    # ----- Valores fixos para R e C -----
    R = 1000        # 1 kΩ
    C = 1e-6        # 1 µF

    # ----- Constante de tempo -----
    tau = R * C
    print(f"\nConstante de tempo (tau = R*C): {tau} segundos\n")

    # ----- Cálculo do tempo para atingir a tensão alvo -----
    tempo_para_V_alvo = -tau * np.log(V_alvo / V0)

    print("\n========================================")
    print(f" TEMPO PARA ATINGIR {V_alvo} V = {tempo_para_V_alvo:.6f} s")
    print("========================================\n")

    # ----- Vetor de tempo (vai um pouco além do tempo alvo) -----
    t = np.linspace(0, tempo_para_V_alvo * 1.3, 250)

    # ----- Função da tensão -----
    V = V0 * np.exp(-t / tau)

    # ----- Listagem a cada 5 pontos -----
    print("Valores calculados (a cada 5 pontos):")
    print("Índice\tTempo (s)\tTensão (V)")

    for i in range(0, len(t), 5):
        tempo_atual = t[i]
        tensao_atual = V[i]

        # Verifica se cruzou a tensão alvo
        if tempo_atual >= tempo_para_V_alvo and \
           t[i-5] < tempo_para_V_alvo:
            print("\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"  ATINGIU A TENSÃO ALVO ({V_alvo} V) EM t = {tempo_para_V_alvo:.6f} s")
            print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

        print(f"{i}\t{tempo_atual:.6f}\t{tensao_atual:.6f}")

    # ----- Resumo final -----
    print("\n========================================")
    print(f"RESUMO FINAL:")
    print(f"Tensão inicial: {V[0]:.2f} V")
    print(f"Tensão alvo: {V_alvo} V")
    print(f"Tempo para atingir a tensão alvo: {tempo_para_V_alvo:.6f} segundos")
    print("Limite da tensão quando t → ∞ : 0 V")
    print("========================================\n")

    # ----- GRÁFICO -----
    plt.plot(t, V, label="V(t) = V0 * exp(-t/RC)")
    plt.axhline(V_alvo, linestyle='--', label=f"Tensão alvo = {V_alvo} V")
    plt.axvline(tempo_para_V_alvo, linestyle='--', label=f"t alvo = {tempo_para_V_alvo:.6f} s")
    plt.title("Descarga de um Capacitor RC")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Tensão (V)")
    plt.grid(True)
    plt.legend()
    plt.show()


main()
