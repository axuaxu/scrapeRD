
from pathlib import Path
from django.test import TestCase
import sqlite3
#write reddit subcat
# Create your tests here.

con = sqlite3.connect('..\db.csv')
con.text_factory = str
cur = con.cursor()

#p = Path('../data')
#FileList = list(p.glob('./*.*'))
#print FileList

delSQL = "delete from crawlRD_redditcsv "
print delSQL
cur.execute(delSQL)

con.commit()
