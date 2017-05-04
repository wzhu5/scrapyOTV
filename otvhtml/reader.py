import csv
import sys

f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    for col in reader:
        print col[0]
finally:
    f.close()
