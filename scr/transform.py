import pandas as pd
import json

df_row = pd.read_json("ERP.json")

guest_checks = pd.json_normalize(df_row['guestChecks'])

columns_to_keep = list(guest_checks_df.columns[:guest_checks_df.columns.get_loc('numChkPrntd')+1])


taxes = pd.json_normalize(
    data=df_row['guestChecks'],
    record_path='taxes',
    meta=['guestCheckId']
)
 
detail_lines = pd.json_normalize(
    data=df_row['guestChecks'],
    record_path='detailLines',
    meta=['guestCheckId']
)



print("Guest Checks:")
print(guest_checks.head())

print("\nTaxes:")
print(taxes.head())

print("\nDetail Lines:")
print(detail_lines.head())
