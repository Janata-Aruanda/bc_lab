import pandas as pd
import sqlite3


conn = sqlite3.connect('bc_lab.db')

guest_check_df = pd.read_csv("./data/guest_checks.csv")
taxes_df = pd.read_csv("./data/taxes.csv")
detail_df = pd.read_csv("./data/detail_lines.csv")
menu_df = pd.read_csv("./data/menu_items.csv")


guest_check_df.to_sql("guest_check", conn, if_exists='replace', index=False)
taxes_df.to_sql("taxes", conn, if_exists='replace', index=False)
detail_df.to_sql("detail", conn, if_exists='replace', index=False)
menu_df.to_sql("menu", conn, if_exists='replace', index=False)


conn.close()
