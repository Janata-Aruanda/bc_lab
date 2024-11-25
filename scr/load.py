import sqlite3
import pandas as pd

def connect_db(db: str):
    """Conecta ao banco de dados SQLite e retorna a conexão."""
    conn = sqlite3.connect(f'{db}/cb_lab.db')
    return conn

def ler_data(file_path: str) -> pd.DataFrame:
    """Lê os dados de um arquivo CSV e retorna um DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"Arquivo {file_path} lido com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        return None

def save_sql(df: pd.DataFrame, name_tb: str, conn):
    try:
        df.to_sql(name=name_tb, con=conn, if_exists='replace', index=False)
        print(f"Tabela {name_tb} salva com sucesso no banco de dados.")
    except Exception as e:
        print(f"Erro ao salvar a tabela {name_tb}: {e}")

if __name__ == "__main__":

    # Caminho do banco de dados
    db_path = "./data/gold"

    # Caminhos dos arquivos CSV
    dt_guest = "./data/silver/guest.csv"
    dt_taxes = "./data/silver/taxes.csv"
    dt_details = "./data/silver/details.csv"
    dt_menu_item = "./data/silver/mnitem.csv"

    # Conectando ao banco de dados
    conn = connect_db(db_path)

    # Lendo e salvando os dados no banco
    datasets = {
        "guest_checks": dt_guest,
        "taxes": dt_taxes,
        "detail_lines": dt_details,
        "menu_items": dt_menu_item
    }

    for table_name, file_path in datasets.items():
        df = ler_data(file_path)
        if df is not None:
            save_sql(df, table_name, conn)

    # Fechar a conexão
    conn.close()
    print("Conexão com o banco de dados fechada.")
