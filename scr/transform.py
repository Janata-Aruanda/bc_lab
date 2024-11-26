import json
import pandas as pd

def extract_guest(file_dir: str):
    with open(f"{file_dir}/guestChecks.json", "r") as f:
        guest_raw = json.load(f)

    # Verifica se os dados são um dicionário e converte para lista
    if isinstance(guest_raw, dict):
        guest_raw = [guest_raw]

    # Converte os dados para um DataFrame
    df_guest = pd.DataFrame(guest_raw)
    return df_guest

def extract_taxes(file_dir: str):
    with open(f"{file_dir}/taxes.json", "r") as f:
        taxes_raw = json.load(f)

    # Verifica se os dados são um dicionário e converte para lista
    if isinstance(taxes_raw, dict):
        taxes_raw = [taxes_raw]

    # Converte os dados para um DataFrame
    df_taxes = pd.DataFrame(taxes_raw)
    return df_taxes

def extract_details(file_dir: str):
    with open(f"{file_dir}/detailLines.json", "r") as f:  # Nome corrigido
        details_raw = json.load(f)

    # Verifica se os dados são um dicionário e converte para lista
    if isinstance(details_raw, dict):
        details_raw = [details_raw]

    # Converte os dados para um DataFrame
    df_details = pd.DataFrame(details_raw)
    return df_details

def extract_mnitem(file_dir: str):
    with open(f"{file_dir}/menu_item.json", "r") as f:  # Nome corrigido
        mnitem_raw = json.load(f)

    # Verifica se os dados são um dicionário e converte para lista
    if isinstance(mnitem_raw, dict):
        mnitem_raw = [mnitem_raw]

    # Converte os dados para um DataFrame
    df_mnitem = pd.DataFrame(mnitem_raw)
    return df_mnitem

def relacionar(file_dir: str):
    df_guest = extract_guest(file_dir)
    df_taxes = extract_taxes(file_dir)
    df_details = extract_details(file_dir)
    df_mnitem = extract_mnitem(file_dir)

    # Relacionando entre tabelas
    df_taxes['guestCheckId'] = df_guest['guestCheckId']
    df_details['guestCheckId'] = df_guest['guestCheckId']
    df_mnitem['guestCheckLineItemId'] = df_details['guestCheckLineItemId']

    return df_guest, df_taxes, df_details, df_mnitem

def save_file(df_guest, df_taxes, df_details, df_mnitem, file_destino: str):
    df_guest.to_csv(f"{file_destino}/guest.csv", index=False)
    df_taxes.to_csv(f"{file_destino}/taxes.csv", index=False)
    df_details.to_csv(f"{file_destino}/details.csv", index=False)
    df_mnitem.to_csv(f"{file_destino}/mnitem.csv", index=False)

# Exemplo de uso
if __name__ == "__main__":
    file_directory = "./data/raw"
    file_destino = "./data/silver"

    # Normaliza os dados
    df_guest, df_taxes, df_details, df_mnitem = relacionar(file_directory)

    # Salva os dados processados em arquivos CSV
    save_file(df_guest, df_taxes, df_details, df_mnitem, file_destino)

    print("Arquivos salvos com sucesso em:", file_destino)
