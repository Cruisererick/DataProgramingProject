import DownloadFiles
import ReadTxtFile
import os
import csv
#-*- coding: utf-8 -*-

def main():

    get_data()
    filename = "D://One company//2017-Q3//1325702-MAGNACHIP SEMICONDUCTOR Corp//10-Q-2017-08-04.html"
    folder = "D://Data//2017-Q1"
    #create_csv_tables(folder)
    #create_csv_common_table(folder)
    #load_table()


def create_custom_table(tableName, parameter, folder):
    final_table = {}
    table = []
    for subdir, dirs, files in os.walk(folder):
        if os.path.isdir(files):
            create_custom_table(tableName, parameter, files)
        else:
            for file in files:
                if tableName + ".csv" in str(file):
                    company = subdir.split("\\")
                    table = load_table(file, tableName + ".csv")
                    for lines in table:
                        if parameter in lines:
                            aux = parameter.split(",")
                            touple = [aux[1], aux[2]]
                            final_table[company[1]] = touple



def create_csv_common_table(folder):
    table_dict = {}
    filename = "tables.csv"
    data = []
    import pandas as pd
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
    filename = folder + "//" + tablename
    table_list = []
    file_object = open(filename, 'r')
    for lines in file_object:
        print(lines)
        table_list.append(lines)
    return table_list


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
