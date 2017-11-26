import DownloadFiles
#import ReadTxtFile
import os
import csv
import collections
import pandas as pd
from datetime import datetime
#-*- coding: utf-8 -*-

final_table = collections.OrderedDict()


def main():

    #get_data()
    #filename = "D://One company//2017-Q3//1325702-MAGNACHIP SEMICONDUCTOR Corp//10-Q-2017-08-04.html"
    folder = "E://2017-Q1"
    #create_csv_tables(folder)
    #create_csv_common_table(folder)
    #load_table()


    table = "Consolidated Balance Sheets - USD ()  in Thousands"
    parameter = "Total assets"
    create_custom_dict(table, parameter, folder)
    print(final_table)
    create_custom_table(table, parameter)


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
            for dicts in value:
                try:
                    aux[dates] = dicts[dates]
                except:
                    aux[dates] = 0
        touple = [key, *aux.values()]
        data.append(touple)

    df = pd.DataFrame(data, columns=['Company', *dates_in_time])
    df.to_csv(filename + "//" + table + "_" + parameter + ".csv", index=False)




def create_custom_dict(tableName, parameter, folder):

    table = []
    for subdir, dirs, files in os.walk(folder):
        if len(dirs) > 1:
            for item in dirs:
                create_custom_dict(tableName, parameter, folder + "//" + item)
        else:
            for file in files:
                if tableName + ".csv" == file:
                    company = subdir.split("//")
                    table = load_table(folder, tableName + ".csv")
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
                                dates[1] = dates[1].replace(".", " ").replace(",", " ")
                                try:
                                    datetime_object0 = datetime.strptime(dates[0], '%b %d %Y')
                                    datetime_object1 = datetime.strptime(dates[1], '%b %d %Y')
                                    dates_dict[datetime_object0] = row[1]
                                    dates_dict[datetime_object1] = row[2]
                                    if company[len(company) - 1] in final_table:
                                        final_table[company[len(company) - 1]].append(dates_dict)
                                    else:
                                        aux_list = []
                                        aux_list.append(dates_dict)
                                        final_table[company[len(company) - 1]] = aux_list
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


def create_csv_tables(folder):

    for subdir, dirs, files in os.walk(folder):
        for file in files:
            ReadTxtFile.read_beautiful(file, subdir)




def get_data():
    year = "2016"
    Q1 = open("C://Users//eric//Desktop//Files for XBRL//Index " + year + "//Q1.txt", "r")
    Q2 = open("C://Users//eric//Desktop//Files for XBRL//Index " + year + "//Q2.txt", "r")
    Q3 = open("C://Users//eric//Desktop//Files for XBRL//Index " + year + "//Q3.txt", "r")
    Q4 = open("C://Users//eric//Desktop//Files for XBRL//Index " + year + "//Q4.txt", "r")
    list = [Q1, Q2, Q3, Q4]

    for x in range(0, len(list)):
        DownloadFiles.download(list[x], "Q" + str(x + 1), year)
    print("End")


if __name__ == '__main__':
    main()
