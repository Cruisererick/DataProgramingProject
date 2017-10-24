import re
import urllib.request
import os
#-*- coding: utf-8 -*-
#!/usr/bin/env python


def download():
    file = open("D://Dataprogramming files//Index 2017//Q1.txt", "r")
    i = 0
    r = re.compile('.*\|.*\|.*\|.*\|.*')
    j = 0;
    for line in file:
        if r.match(line):
            if j > 0:
                elements = line.split('|')
                for item in elements:
                    item = item.strip('\n')
                if '/' in elements[1]:
                    name = elements[1].split('/')
                    elements[1] = name[0].strip()
                elif '\\' in elements[1]:
                    name = elements[1].split('\\')
                    elements[1] = name[0].strip()

                url = "https://www.sec.gov/Archives/" + elements[4]
                html = urllib.request.urlopen(url)
                content = html.read()
                filename = 'D://Dataprogramming files//' \
                           + elements[0] + "-" + elements[1] + '//' + elements[2] + "-" + elements[3] + '.xml'
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                content = content.decode("utf-8")
                save = open(filename, 'w')
                try:
                    save.write(content)
                except:
                    print("Crash")
                save.close()
            j += 1

