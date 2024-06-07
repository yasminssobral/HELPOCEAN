import csv

# Dados das ONGs nos bairros especificados
ongs = [
    {"Nome da ONG": "MarLimpo", "Latitude": -23.5556, "Longitude": -46.6863, "Região": "Vila Madalena"},
    {"Nome da ONG": "EcoMar", "Latitude": -23.5740, "Longitude": -46.6238, "Região": "Aclimação"},
    {"Nome da ONG": "VidaMar", "Latitude": -23.5320, "Longitude": -46.5890, "Região": "Pari"},
    {"Nome da ONG": "LitoralVivo", "Latitude": -23.5500, "Longitude": -46.6020, "Região": "Mooca"},
    {"Nome da ONG": "LimpezaCosteira", "Latitude": -23.5750, "Longitude": -46.5880, "Região": "Aricanduva"},
    {"Nome da ONG": "OndaAzul", "Latitude": -23.5660, "Longitude": -46.6720, "Região": "Pinheiros"},
    {"Nome da ONG": "PraiaLimpa", "Latitude": -23.5500, "Longitude": -46.6220, "Região": "Canindé"},
    {"Nome da ONG": "VerdeMar", "Latitude": -23.5860, "Longitude": -46.6800, "Região": "Itaim Bibi"},
    {"Nome da ONG": "ProteçãoMarinha", "Latitude": -23.5890, "Longitude": -46.6380, "Região": "Vila Mariana"},
    {"Nome da ONG": "PlanetaOceano", "Latitude": -23.5790, "Longitude": -46.6150, "Região": "Ipiranga"},
    {"Nome da ONG": "MarVivo", "Latitude": -23.5420, "Longitude": -46.5820, "Região": "Tatuapé"},
    {"Nome da ONG": "LimpandoMares", "Latitude": -23.5630, "Longitude": -46.5740, "Região": "Vila Formosa"},
    {"Nome da ONG": "OceanoLivre", "Latitude": -23.5720, "Longitude": -46.5680, "Região": "Carrão"},
    {"Nome da ONG": "Aquamar", "Latitude": -23.5540, "Longitude": -46.5980, "Região": "Liberdade"}
]

# Nome do arquivo CSV
nome_arquivo = "ongs_localizacao.csv"

# Escrever dados das ONGs para o arquivo CSV
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    cabecalho = ["Nome da ONG", "Latitude", "Longitude", "Região"]
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)

    escritor_csv.writeheader()
    for ong in ongs:
        escritor_csv.writerow(ong)

print(f"Arquivo CSV '{nome_arquivo}' gerado com sucesso!")
