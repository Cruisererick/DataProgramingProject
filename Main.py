import DownloadFiles
import ReadTxtFile
#-*- coding: utf-8 -*-

def main():

    #get_data()
    filename = "D://One company//2017-Q3//1325702-MAGNACHIP SEMICONDUCTOR Corp//10-Q-2017-08-04.html"
    ReadTxtFile.read_beautiful(filename)

def get_data():
    year = "2007"
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
