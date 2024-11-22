import pandas as pd

# Ler o arquivo JSON
data = pd.read_json('ERP.json')

# Variaveis 
taxes_list = []
detail_lines_list = []
menu_items_list = []

# Extrair 'guestChecks' em um DataFrame
guest_checks_all = pd.json_normalize(data['guestChecks'])

# Verifique se 'seatNum' existe nas colunas
if 'numChkPrntd' in guest_checks_all.columns:
    guest_checks_df = guest_checks_all.loc[:, :'numChkPrntd']
else:
    ("A coluna 'numChkPrntd' não foi encontrada no DataFrame 'guest_checks'.")


# Extrair 'taxes' com referência ao 'guestCheckId'
for guest_check in data['guestChecks']:
    guest_check_id = guest_check['guestCheckId']
    taxes = guest_check.get('taxes', [])
    for tax in taxes:
        tax_record = tax.copy()
        tax_record['guestCheckId'] = guest_check_id  # Adicionar referência ao guestCheckId
        taxes_list.append(tax_record)
taxes_df = pd.DataFrame(taxes_list)

# Extrair 'detailLines' e 'menuItem' com referências apropriadas
for guest_check in data['guestChecks']:
    guest_check_id = guest_check['guestCheckId']
    detail_lines = guest_check.get('detailLines', [])
    for detail_line in detail_lines:
        detail_line_record = detail_line.copy()
        detail_line_record['guestCheckId'] = guest_check_id  # Referência ao guestCheckId
        
        # Extrair 'menuItem' e remover do 'detail_line_record'
        menu_item = detail_line_record.pop('menuItem', None)
        
        # Adicionar 'detail_line_record' à lista
        detail_lines_list.append(detail_line_record)
        
        # Se 'menuItem' existir, adicionar à lista de 'menu_items'
        if menu_item:
            menu_item_record = menu_item.copy()
            menu_item_record['guestCheckLineItemId'] = detail_line['guestCheckLineItemId']  # Referência ao detailLine
            menu_items_list.append(menu_item_record)
            
# Criando dataframe            
detail_lines_df = pd.DataFrame(detail_lines_list)
menu_items_df = pd.DataFrame(menu_items_list)


#Salvando em formato de arquivo otimizado

guest_checks_df.to_csv("./data/guest_checks.csv")
taxes_df.to_csv("./data/taxes.csv")
detail_lines_df.to_csv("./data/detail_lines.csv")
menu_items_df.to_csv("./data/menu_items.csv")