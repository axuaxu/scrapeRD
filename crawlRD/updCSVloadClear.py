
from pathlib import Path
from django.test import TestCase
import csv, sqlite3

# set the upload csv file list,load=1

con = sqlite3.connect('..\db.csv')
con.text_factory = str
cur = con.cursor()

updateSQL =  "update crawlRD_redditsub set load=0 "
cur.execute(updateSQL)
con.commit()
cur.execute("select * from crawlRD_redditsub where  load=1 ")
all_rows = cur.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    #pass
