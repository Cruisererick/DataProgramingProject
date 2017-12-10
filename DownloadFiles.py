import re
import urllib.request
import os
#-*- coding: utf-8 -*-
#!/usr/bin/env python


def download(file, Q, year, savefolder):

        i = 0
        r = re.compile('.*\|.*\|.*\|.*\|.*')
        j = 0
        counter = 0
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
                    if elements[1] == "MAGNACHIP SEMICONDUCTOR Corp" or elements[1] is not None:
                        url = "https://www.sec.gov/Archives/" + elements[4]
                        try:
                            html = urllib.request.urlopen(url)

                            content = html.read()
                            filename = savefolder + '//' + str(year) + "-" + Q + '//' \
                                       + elements[0] + "-" + elements[1] + '//' + elements[2] + "_" + elements[3] + '.xml'
                            os.makedirs(os.path.dirname(filename), exist_ok=True)
                            content = content.decode("utf-8")
                            save = open(filename, 'w')
                            try:
                                save.write(content)
                                counter += 1
                                print(counter)
                                if counter > 1000:
                                    pass
                            except:
                                print(url)
                                print(Q)
                            save.close()
                        except:
                            print(url)
                            print(Q)
                j += 1
