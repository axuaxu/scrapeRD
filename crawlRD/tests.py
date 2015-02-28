
from pathlib import Path
from django.test import TestCase
import csv, sqlite3

# Create your tests here.

con = sqlite3.connect('..\db.csv')
con.text_factory = str
cur = con.cursor()
cur.execute("select id,tid,count(*),catName from crawlRD_redditcsvcat group by tid having count(*)>1")
#cur.execute("delete from crawlRD_redditcsvcat where id = 29102")
all_rows = cur.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
con.commit()