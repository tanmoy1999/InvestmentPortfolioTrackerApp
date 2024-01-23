import pandas as pd
import requests
import csv
import json

k = 'https://www.amfiindia.com/spages/NAVAll.txt'
k = 'https://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=19-JAN-2024'

def mf_report(dt):
    k = 'https://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=' + str(dt)
    response = requests.get(k)
    df = pd.DataFrame(columns=['Scheme Code', 'Scheme Name', 'ISIN Div Payout/ISIN Growth', 'ISIN Div Reinvestment', 'Net Asset Value', 'Repurchase Price', 'Sale Price', 'Date\r'])
    data = response.text.split("\n")
    for scheme_data in data:
        
        if ";" in scheme_data:
            # print(scheme_data)
            scheme = scheme_data.split(";")
            # print(scheme)
            scheme[7] = scheme[7].replace('\r','')
            if '2024' in scheme[7]:
                df.loc[len(df)] = scheme
    return df

df1 = mf_report('19-JAN-2024')
df2 = mf_report('18-JAN-2024')

result_df = pd.merge(df1, df2, on='Scheme Code', how='inner')
selected_columns = result_df[['Scheme Code','Scheme Name_x','Date\r_x','Net Asset Value_x','Date\r_y','Net Asset Value_y']]


# Filter

pgim = k[k['Scheme Code'].str.contains('125307', case=False)]
icici = k[k['Scheme Code'].str.contains('125307', case=False)]
# icici - 5682   parakh parik - 6744  tata digital - 135795 pgim - 125307 quant - 120828

