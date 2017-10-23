import re



def download():
    file = open("C://Users//eric//Desktop//Files for XBRL//Index 2017//Q1.txt", "r")
    i = 0
    r = re.compile('%s|%s|%s|%s|%s')
    for line in file:

        print(line)
        if r.match(line) is not None:
            print('matches')
        if i > 10:
            break
        i += 1
