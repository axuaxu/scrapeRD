
from pathlib import Path
from django.test import TestCase
import sqlite3
#write reddit subcat
# Create your tests here.

con = sqlite3.connect('..\db.csv')
con.text_factory = str
cur = con.cursor()

p = Path('../data')
FileList = list(p.glob('./*.*'))
#print FileList

for w in FileList:
    FileName = w.parts[2]
    #print FileName
    insertSQL = "insert into crawlRD_redditsub (subcat) values ('" + FileName + "')"
    print insertSQL
    cur.execute(insertSQL)

con.commit()
