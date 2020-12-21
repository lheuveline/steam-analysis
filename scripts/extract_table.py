import sys
import gzip

'''
Extract table from MySQL dump file
use like this:
python extract_table.py filename.gz table_name > extract.txt
'''

with gzip.open(sys.argv[1],'rb') as f:
    bIn = False
    for line in f:
        line = line.strip()
        #LOCK TABLES `table_name` WRITE;        
        if line.startswith("LOCK TABLES"):
            None
        if line == "LOCK TABLES `%s` WRITE;" % sys.argv[2]:
            bIn = True
        elif line == "UNLOCK TABLES;":
            bIn = False
        elif bIn:           
            print line
