#%%
import pandas as pd
import requests
import csv
import json

def mffull():
    k = 'https://www.amfiindia.com/spages/NAVAll.txt'
    response = requests.get(k)
    df = pd.DataFrame(columns=['Scheme Code','ISIN Div Payout/ ISIN Growth','ISIN Div Reinvestment','Scheme Name','Net Asset Value','Date'])
    data = response.text.split("\n")
    for scheme_data in data:
        if ";INF" in scheme_data:
            scheme = scheme_data.split(";")
            scheme[5] = scheme[5].replace('\r','')
            if '2023' in scheme[5]:
                df.loc[len(df)] = scheme
                print('2023')
    return df

mffull().to_csv('mf.csv')


csv_file = 'mf.csv'
json_file = 'data.json'

data = {}

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        scheme_name = row['Scheme Name']
        data = {
            'Scheme Name': row['Scheme Name'],
            'Scheme Code': int(row['Scheme Code']),
            'ISIN Div Payout/ ISIN Growth': row['ISIN Div Payout/ ISIN Growth'],
            'ISIN Div Reinvestment': row['ISIN Div Reinvestment'],
            'Net Asset Value': float(row['Net Asset Value']),
            'Date': row['Date']
        }

with open(json_file, 'w') as file:
    json.dump(data, file, indent=2)

print(f"CSV file '{csv_file}' converted to JSON file '{json_file}' successfully.")

# https://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=20-FEB-2022

# %%
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

df1 = mf_report('22-JAN-2024')
df2 = mf_report('19-JAN-2024')

result_df = pd.merge(df1, df2, on='Scheme Code', how='inner')
selected_columns = result_df[['Scheme Code','Scheme Name_x','Date\r_x','Net Asset Value_x','Date\r_y','Net Asset Value_y']]

result = selected_columns.loc[(selected_columns['Scheme Code'] == '141841') | (selected_columns['Scheme Code'] == '122639') | (selected_columns['Scheme Code'] == '135795') | (selected_columns['Scheme Code'] == '125307') | (selected_columns['Scheme Code'] == '120828')]
# icici - 141841   parakh parik - 122639  tata digital - 135795 pgim - 125307 quant - 120828
result

# %%
from datetime import timedelta, date

def generate_weekday_dates(start_date, end_date):
    delta = timedelta(days=1)
    current_date = start_date
    weekday_dates = []

    while current_date <= end_date:
        # Check if the current date is not a Saturday or Sunday
        if current_date.weekday() < 5:  # Monday to Friday (0 to 4)
            weekday_dates.append(current_date)
        
        # Move to the next day
        current_date += delta

    return weekday_dates

# Example: Generate a list of dates excluding weekends for a specific range
start_date = date(2024, 1, 1)
end_date = date(2024, 1, 31)

result_dates = generate_weekday_dates(start_date, end_date)

# Display the result
print(result_dates)
# %%
