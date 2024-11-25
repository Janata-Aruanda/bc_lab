import pandas as pd

# Carrega os dados do JSON
data = pd.read_json('ERP.json')

# Normaliza os dados até o nível desejado
guest_checks_row = pd.json_normalize(
    data['guestChecks'],
    max_level=1  
)
# Remove as colunas de campos aninhados, se ainda estiverem presentes
guest_checks = guest_checks_row.drop(columns=['taxes', 'detailLines'])

taxes_df = pd.json_normalize(
    data=data['guestChecks'],
    record_path='taxes',
    meta=['guestCheckId']
)

# Exibe as primeiras linhas do DataFrame
print(guest_checks_df.head(1))
