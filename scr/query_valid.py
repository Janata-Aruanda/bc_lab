import pandas as pd
import sqlite3

conn = sqlite3.connect('./data/gold/cb_lab.db')


df_guest = pd.read_sql_query("SELECT * FROM guest_checks", conn)

df_taxes = pd.read_sql_query("SELECT * FROM taxes", conn)

df_detail = pd.read_sql_query("SELECT * FROM detail_lines", conn)

df_nmitem = pd.read_sql_query("SELECT * FROM menu_items", conn)


print(df_guest.head(), "\t")
print(df_taxes.head(), "\t")
print(df_detail.head(), "\t")
print(df_nmitem.head(), "\t")

conn.close()