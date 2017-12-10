import DownloadFiles
import ReadTxtFile
import os
import csv
import collections
import pandas as pd
from datetime import datetime
import re
#-*- coding: utf-8 -*-

final_table = collections.OrderedDict()


def tables_per_quater(folder, table_name):
     for subdir, dirs, files in os.walk(folder):
        create_csv_tables(dirs, table_name)


def main():
    index_data = "C://Users//eric//Desktop//Files for XBRL//Index "
    save_folder = 'C://DataPrograming'
    year = 2016
    table = "Consolidated Balance Sheets"
    parameter = "Total assets"
    get_data(index_data, year, save_folder)


    #create_csv_tables(save_folder, table)


    #create_custom_dict(table, parameter, save_folder)
    #create_custom_table(table, parameter)



def create_custom_table(table, parameter):
    dates_in_time = set()
    data = []
    filename = "Custom Tables"

    for key, value in final_table.items():
        aux = []
        for dicts in value:
            for key_date, value_date in dicts.items():
                try:
                    aux.append(value_date)
                    dates_in_time.add(key_date)
                except:
                    pass
    dates_in_time = sorted(dates_in_time)

    for key, value in final_table.items():
        aux = collections.OrderedDict()
        for dates in dates_in_time:
            isIn = False
            for dicts in value:
                try:
                    aux[dates] = float(dicts[dates].replace(",", ""))
                    isIn = True
                except:
                    pass
            if isIn == False:
                aux[dates] = 0
        touple = [key, *aux.values()]
        data.append(touple)

    df = pd.DataFrame(data, columns=['Company', *dates_in_time])
    df.to_csv(filename + "//" + table + "_" + parameter + ".csv", index=False)


def get_date(date):
    realDate = datetime.strptime(date[0], '%Y-%m-%d').date()
    year = realDate.year
    Q1 = datetime.strptime('3-31' + '-' + str(year), '%m-%d-%Y').date()
    Q2 = datetime.strptime('6-30' + '-' + str(year), '%m-%d-%Y').date()
    Q3 = datetime.strptime('9-30' + '-' + str(year), '%m-%d-%Y').date()
    Q4 = datetime.strptime('12-31' + '-' + str(year), '%m-%d-%Y').date()
    QN = datetime.strptime('3-31' + '-' + str(year + 1), '%m-%d-%Y').date()
    QP = datetime.strptime('12-31' + '-' + str(year - 1), '%m-%d-%Y').date()
    if Q1 < realDate < Q2:
        return Q1
    if Q2 < realDate < Q3:
        return Q2
    if Q3 < realDate < Q4:
        return Q3
    if Q4 < realDate < QN:
        return Q4
    if QP < realDate < Q1:
        return QP


def create_custom_dict(tableName, parameter, folder):

    table = []
    for subdir, dirs, files in os.walk(folder):
        if len(dirs) > 1:
            for item in dirs:
                create_custom_dict(tableName, parameter, folder + "//" + item)
        else:
            for file in files:
                if tableName.lower() in file.lower() or "Consolidated Balance Sheets".lower() in file.lower():
                    company = subdir.split("//")
                    company = company[len(company) - 1].split("\\")
                    company = company[len(company) - 1]
                    table = load_table(subdir, file)
                    date = file.split("_")
                    date = get_date(date)
                    if table is not None:
                        counter = 0
                        dates = []
                        dates_dict = {}
                        for row in table:
                            if counter is 0:
                                dates.append(row[1])
                                dates.append(row[2])
                                counter += 1
                            if parameter == row[0]:
                                dates[0] = dates[0].replace(".", " ").replace(",", " ")
                                #dates[1] = dates[1].replace(".", " ").replace(",", " ")
                                try:
                                    datetime_object0 = date
                                    #datetime_object1 = datetime.strptime(dates[1], '%b %d %Y')
                                    number = re.sub('[^0-9.,]', '', row[1])
                                    dates_dict[datetime_object0] = number
                                    #dates_dict[datetime_object1] = row[2]
                                    if company in final_table:
                                        final_table[company].append(dates_dict)
                                    else:
                                        aux_list = []
                                        aux_list.append(dates_dict)
                                        final_table[company] = aux_list
                                except:
                                    pass


def create_csv_common_table(folder):
    table_dict = {}
    filename = "tables.csv"
    data = []
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            if ".csv" in str(file):
                table_name = str(file)[:-4]
                company = subdir.split("\\")
                if table_name in table_dict:
                    table_dict[table_name].append(company[1])
                else:
                    list = []
                    list.append(company[1])
                    table_dict[table_name] = list
    for tables in table_dict:
        tople = [tables, table_dict[tables]]
        data.append(tople)

    df = pd.DataFrame(data, columns=['Table', 'Company'])
    df.to_csv(filename, index=False)


def load_table(folder, tablename):
    try:
        filename = folder + "//" + tablename
        table_list = []
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if len(row) > 0:
                    table_list.append(row)
        return table_list
    except:
        return None


def create_csv_tables(folder, table_name):

    for subdir, dirs, files in os.walk(folder):
        if len(dirs) > 0:
            for one_folder in dirs:
                create_csv_tables(folder + "//" + one_folder, table_name)
        else:
            for file in files:
                if '.csv' in file:
                    print(subdir + '//' + file)
                    ReadTxtFile.read_beautiful(file, subdir, table_name)



def get_data(index_folder, year, savefolder):
    index_folder = index_folder
    Q1 = open(index_folder + str(year) + "//Q1.txt", "r")
    Q2 = open(index_folder + str(year) + "//Q2.txt", "r")
    Q3 = open(index_folder + str(year) + "//Q3.txt", "r")
    Q4 = open(index_folder + str(year) + "//Q4.txt", "r")
    list = [Q1, Q2, Q3, Q4]

    for x in range(0, 4):
        DownloadFiles.download(list[x], "Q" + str(x + 1), year, savefolder)
    print("End")


if __name__ == '__main__':
    main()
