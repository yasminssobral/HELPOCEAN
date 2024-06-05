import csv

# Dados das ONGs
ongs = [
    {"Nome da ONG": "MarLimpo", "Latitude": -23.7134, "Longitude": -46.6617, "Região": "Sul"},
    {"Nome da ONG": "EcoMar", "Latitude": -23.6862, "Longitude": -46.6453, "Região": "Sul"},
    {"Nome da ONG": "VidaMar", "Latitude": -23.7045, "Longitude": -46.6431, "Região": "Sul"},
    {"Nome da ONG": "LitoralVivo", "Latitude": -23.7261, "Longitude": -46.6659, "Região": "Sul"},
    {"Nome da ONG": "LimpezaCosteira", "Latitude": -23.6954, "Longitude": -46.6287, "Região": "Sul"},
    {"Nome da ONG": "OndaAzul", "Latitude": -23.7218, "Longitude": -46.6234, "Região": "Sul"},
    {"Nome da ONG": "PraiaLimpa", "Latitude": -23.7129, "Longitude": -46.6355, "Região": "Sul"},
    {"Nome da ONG": "VerdeMar", "Latitude": -23.6809, "Longitude": -46.6268, "Região": "Sul"},
    {"Nome da ONG": "ProteçãoMarinha", "Latitude": -23.7397, "Longitude": -46.6159, "Região": "Sul"},
    {"Nome da ONG": "PlanetaOceano", "Latitude": -23.7057, "Longitude": -46.5931, "Região": "Leste"},
    {"Nome da ONG": "MarVivo", "Latitude": -23.6896, "Longitude": -46.5823, "Região": "Leste"},
    {"Nome da ONG": "LimpandoMares", "Latitude": -23.6713, "Longitude": -46.5915, "Região": "Leste"},
    {"Nome da ONG": "OceanoLivre", "Latitude": -23.7084, "Longitude": -46.5692, "Região": "Leste"},
    {"Nome da ONG": "Aquamar", "Latitude": -23.7256, "Longitude": -46.5751, "Região": "Leste"},
    {"Nome da ONG": "VidaMarítima", "Latitude": -23.6982, "Longitude": -46.5598, "Região": "Leste"},
    {"Nome da ONG": "ProjetoOndas", "Latitude": -23.6817, "Longitude": -46.5426, "Região": "Leste"},
    {"Nome da ONG": "PraiaPreservada", "Latitude": -23.7148, "Longitude": -46.5426, "Região": "Leste"},
    {"Nome da ONG": "AmigosdoMar", "Latitude": -23.7315, "Longitude": -46.5587, "Região": "Leste"},
    {"Nome da ONG": "OndaVerde", "Latitude": -23.6752, "Longitude": -46.5185, "Região": "Leste"},
    {"Nome da ONG": "ONGMarítima", "Latitude": -23.7043, "Longitude": -46.5279, "Região": "Leste"},
    {"Nome da ONG": "MarAzul", "Latitude": -23.6792, "Longitude": -46.5088, "Região": "Norte"},
    {"Nome da ONG": "LitoralProtegido", "Latitude": -23.7109, "Longitude": -46.5079, "Região": "Norte"},
    {"Nome da ONG": "LimpezaMarinha", "Latitude": -23.6947, "Longitude": -46.4886, "Região": "Norte"},
    {"Nome da ONG": "OceanoLimpo", "Latitude": -23.7254, "Longitude": -46.4861, "Região": "Norte"},
    {"Nome da ONG": "EcoMarinho", "Latitude": -23.6885, "Longitude": -46.4674, "Região": "Norte"},
    {"Nome da ONG": "SOSMar", "Latitude": -23.7125, "Longitude": -46.4765, "Região": "Norte"},
    {"Nome da ONG": "PreservaçãoCosteira", "Latitude": -23.7046, "Longitude": -46.4574, "Região": "Norte"},
    {"Nome da ONG": "PraiaSustentável", "Latitude": -23.6805, "Longitude": -46.4461, "Região": "Norte"},
    {"Nome da ONG": "MarPreservado", "Latitude": -23.7018, "Longitude": -46.4373, "Região": "Norte"},
    {"Nome da ONG": "LimpandoPraias", "Latitude": -23.6734, "Longitude": -46.4242, "Região": "Norte"},
    {"Nome da ONG": "MaréLimpa", "Latitude": -23.7132, "Longitude": -46.4155, "Região": "Norte"},
    {"Nome da ONG": "ONGAmbiental", "Latitude": -23.6943, "Longitude": -46.3961, "Região": "Norte"},
    {"Nome da ONG": "SalvandoOceanos", "Latitude": -23.7259, "Longitude": -46.3972, "Região": "Norte"},
    {"Nome da ONG": "VidaCosteira", "Latitude": -23.6894, "Longitude": -46.3768, "Região": "Norte"},
    {"Nome da ONG": "ProjetoMarinho", "Latitude": -23.7108, "Longitude": -46.3679, "Região": "Norte"},
    {"Nome da ONG": "OndaLimpa", "Latitude": -23.7052, "Longitude": -46.3456, "Região": "Norte"},
    {"Nome da ONG": "MaréViva", "Latitude": -23.6785, "Longitude": -46.3487, "Região": "Norte"},
    {"Nome da ONG": "AmigosdoMarinho", "Latitude": -23.6973, "Longitude": -46.3293, "Região": "Norte"},
    {"Nome da ONG": "MarSaudável", "Latitude": -23.7161, "Longitude": -46.3167, "Região": "Norte"},
    {"Nome da ONG": "OceanoVivo", "Latitude": -23.6921, "Longitude": -46.2984, "Região": "Norte"}
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
