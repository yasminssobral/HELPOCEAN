import csv
import random

# Gera dados simulados de lixo no oceano - CHATGPT
def gerar_dados_lixo_oceano():
    with open('dados_lixo_oceano.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Ano', 'Quantidade de Lixo no Oceano (toneladas)'])
        quantidade_lixo = 500000  # Quantidade inicial de lixo
        for ano in range(2014, 2025):
            # Aumenta a quantidade de lixo com tendência crescente e flutuações aleatórias para simular a realidade
            tendencia = random.uniform(1.05, 1.1)  # Tendência de crescimento entre 5% e 10%
            quantidade_lixo *= tendencia
            quantidade_lixo += random.uniform(-20000, 20000)  # Flutuações aleatórias
            writer.writerow([ano, round(quantidade_lixo)])

if __name__ == "__main__":
    gerar_dados_lixo_oceano()
