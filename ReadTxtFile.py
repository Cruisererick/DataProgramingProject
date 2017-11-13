from xbrl import XBRLParser, GAAP, GAAPSerializer
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import csv
import html5lib
import urllib.request
import re
import unicodedata

def readFile(file):
    xbrl_parser = XBRLParser()

    xbrl = xbrl_parser.parse(file)
    gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20131228", context="current", ignore_errors=0)
    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)
    x = result.find_all("table")
    print(x)


def pandasway(file):
    df_list = pd.read_html(file)

    for i, df in enumerate(df_list):
        print(df)
        if "Accumulated Other Comprehensive Income (Loss) - Schedule of Accumulated Other Comprehensive Income (Loss) (Detail) - USD ($)$ in Thousands" in df.iloc[0]:
            filename = 'D://One company//2017-Q3//1325702-MAGNACHIP SEMICONDUCTOR Corp//table {}.csv'
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            df.to_csv(filename.format(i))


def read_beautiful(file, folder):
    file = folder + '//' + file
    open_file = open(file)
    beatifull = bs(open_file)
    tables = beatifull.find_all("table", attrs={'class': 'report'})
    list_tables = []
    counter = 0
    for table in tables:
        title = table.find('strong')
        headers = [str(header.text) for header in table.find_all('th')]
        title = str(headers[0]).replace('\\xc2', '').replace('$', '').replace('"', '').replace('\\xa0', '').replace('\\n', '').replace("'", '').replace('[', '').replace(']', '').replace('\\', '').replace('/', '')
        rows = []
        for row in table.find_all('tr'):
            rows.append([str(val.text.encode('utf8'))[1:].replace('\\xc2', '').replace('$', '').replace('"', '').replace('\\xa0', '').replace('\\n', '').replace("'", '') for val in row.find_all('td')])
        filename = folder + '//' + title + '.csv'
        counter += 1
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        except:
            filename = folder + '//table' + str(counter) + '.csv'
            counter += 1
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        try:
            with open(filename, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(row for row in rows if row)
        except:
            print(filename)


