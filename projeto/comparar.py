import csv
import matplotlib.pyplot as plt

# Carregar dados do arquivo CSV
def carregar_dados(arquivo):
    anos = []
    quantidades = []
    with open(arquivo, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            anos.append(int(row[0]))
            quantidades.append(float(row[1]))
    return anos, quantidades

# Gera gráfico de comparação
def gerar_grafico_comparacao():
    # Dados do oceano
    anos_oceano, quantidades_oceano = carregar_dados('dados_lixo_oceano.csv')

    # Carrega dados da praia
    anos_praia, quantidades_praia = carregar_dados('dados_lixo_praia.csv')

    # Monta gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(anos_oceano, quantidades_oceano, marker='o', linestyle='-', color='b', label='Lixo no Oceano')
    plt.plot(anos_praia, quantidades_praia, marker='o', linestyle='-', color='r', label='Lixo na Praia')
    plt.title('Comparação de Quantidade de Lixo no Oceano e na Praia (2014-2024)')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade de Lixo (toneladas)')
    plt.xticks(range(2014, 2025))
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('comparacao_lixo_oceano_praia.png')
    plt.show()

if __name__ == "__main__":
    gerar_grafico_comparacao()
