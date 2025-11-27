# Simulação da Descarga de um Capacitor RC

Este repositório contém um código em Python que simula a **descarga de um capacitor** em um circuito RC utilizando a equação exponencial:

\[
V(t) = V_0 \cdot e^{-t/(RC)}
\]

O programa solicita ao usuário apenas:
- **Tensão inicial (V0)**
- **Tensão alvo (V_alvo)**

Os valores de **R** e **C** são mantidos fixos no código, representando um circuito simples onde:
- **R = 1000 Ω (1 kΩ)**
- **C = 1 µF**

O objetivo é determinar:
- O **tempo necessário** para que o capacitor atinja a tensão desejada.
- A exibição da descarga do capacitor **a cada 5 pontos**.
- Destaque do momento exato em que a tensão alvo é atingida.
- Exibição de um **gráfico da curva de descarga**.

---

## 🔧 Funcionalidades do Código

- Cálculo automático da constante de tempo **τ = R·C**.
- Cálculo do tempo exato em que a tensão atinge o valor solicitado.
- Lista dos valores de tempo e tensão a cada 5 pontos da simulação.
- Destaque em console quando a tensão alvo é atingida.
- Gráfico gerado automaticamente usando `matplotlib`.

---

## 🖥️ Exemplo de Gráfico

Adicione abaixo uma imagem do gráfico gerado pelo código:

<img src="Grafico.png"></img>

---

## 📌 Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências:

```
pip install numpy matplotlib
```

3. Execute o arquivo Python:

```
python nome_do_arquivo.py
```

---

## 📘 Explicação Matemática

A tensão no capacitor durante a descarga segue a equação:

\[
V(t) = V_0 e^{-t/RC}
\]

Isolando \( t \) para calcular o tempo até a tensão alvo:

\[
t = -RC \cdot \ln\left( \frac{V_{alvo}}{V_0} \right)
\]

Esse valor é exibido de forma destacada durante a execução.

---

## 🧾 Código Completo

O código completo está disponível no repositório.

---
