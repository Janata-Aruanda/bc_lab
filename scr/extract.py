import json
import os

def desmembrar_json(arquivo_json, saida_base):
    # Verifica se o diretório de saída existe, caso contrário, cria
    os.makedirs(saida_base, exist_ok=True)

    with open(arquivo_json, 'r') as f:
        data = json.load(f)

    for guest_check in data['guestChecks']:
        # Informações básicas do cheque
        cheque_basico = {k: v for k, v in guest_check.items() if k not in ['taxes', 'detailLines']}
        with open(f"{saida_base}/guestChecks.json", 'w') as f:
            json.dump(cheque_basico, f, indent=4)

        # Informações dos impostos
        with open(f"{saida_base}/taxes.json", 'w') as f:
            json.dump(guest_check['taxes'], f, indent=4)

        # Informações das linhas de detalhe e itens do menu
        for idx, detail_line in enumerate(guest_check['detailLines']):
            # Remove a chave 'menuItem' para salvar somente os detalhes
            detail_line_without_menu_item = {k: v for k, v in detail_line.items() if k != 'menuItem'}
            with open(f"{saida_base}/detailLines.json", 'w') as f:
                json.dump(detail_line_without_menu_item, f, indent=4)

            # Salva o menuItem separado
            if 'menuItem' in detail_line:
                with open(f"{saida_base}/menu_item.json", 'w') as f:
                    json.dump(detail_line['menuItem'], f, indent=4)

if __name__ == "__main__":
    # Exemplo de uso
    arquivo_entrada = "ERP.json"
    pasta_saida = "data/raw"
    desmembrar_json(arquivo_entrada, pasta_saida)
