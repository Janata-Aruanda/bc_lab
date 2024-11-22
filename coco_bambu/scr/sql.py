import sqlite3
import pandas


conn = sqlite3.connect('bc_lab.db')


guest_checks = pandas.read_sql("SELECT * FROM guest_check", conn)

taxes_df = pandas.read_sql("SELECT * FROM taxes", conn)

detail_lines = pandas.read_sql("SELECT * FROM detail", conn)

menu_items = pandas.read_sql("SELECT * FROM menu", conn)


print(guest_checks)
print("\t")
print(taxes_df)
print("\t")
print(detail_lines)
print("\t")
print(menu_items)