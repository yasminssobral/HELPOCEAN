import csv
import random

# Gera dados simulados de lixo nas praias - CHATGPT
def gerar_dados_lixo_praia():
    with open('dados_lixo_praia.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Ano', 'Quantidade de Lixo na Praia (toneladas)'])
        quantidade_lixo = 200000  # Quantidade inicial de lixo
        for ano in range(2014, 2025):
            # Aumentar a quantidade de lixo com tendência crescente e flutuações aleatórias
            tendencia = random.uniform(1.05, 1.1)  # Tendência de crescimento entre 5% e 10%
            quantidade_lixo *= tendencia
            quantidade_lixo += random.uniform(-10000, 10000)  # Flutuações aleatórias
            writer.writerow([ano, round(quantidade_lixo)])

if __name__ == "__main__":
    gerar_dados_lixo_praia()
