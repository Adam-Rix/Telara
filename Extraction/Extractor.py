import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

# parsing a site
def parse_site(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table', class_=lambda x: x != 'navbox') # Need to understand, why the exeption isnt work!!!
    return tables

# Extractin the data from the site (tables)
def download_table(tables, filename):
    output_dir = 'Extraction/Saved_tables'  # Diretory for save
    os.makedirs(output_dir, exist_ok=True)  # Creating the save-folder

    for _, table in enumerate(tables, 1):
        df = pd.read_html(str(table))[0]

        # df_to_xml
        xlsx_filename = f"{filename}--{_}.xlsx"
        xlsx_path = os.path.join(output_dir, xlsx_filename)
        df.to_excel(xlsx_path, index=False)  # Сохранение в XML

        print(f"Таблица {_} сохранена в файл {xlsx_filename}")