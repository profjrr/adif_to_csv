from adif2csv import adif2csv
import sys

if len(sys.argv)!=2:
    print("Error: Expected python main.py <ADIF>")
    exit()
else:
    cvt=adif2csv(False)
    cvt.process(sys.argv[1])
    for a in cvt.dump():
        print(''+a, end='')
