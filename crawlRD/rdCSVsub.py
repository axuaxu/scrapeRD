__author__ = 'Anne'
import csv, sqlite3
from datetime import datetime

con = sqlite3.connect('..\db.csv')
con.text_factory = str
cur = con.cursor()
#cur.execute("CREATE TABLE crawlRD_redditcsv (created_utc, score,domain,tid,title,author,ups,downs,num_comments,"
#            "permalink,selftext,link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,"
#            "author_flair_css_class,is_self,name,url,distinguished);")



with open('arma.txt','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    #created_utc,score,domain,id,title,author,ups,downs,num_comments,permalink,selftext,
    # link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,author_flair_css_class,
    # is_self,name,url,distinguished
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['created_utc'],i['score'],i['domain'],i['id'],i['title'],i['author'],i['ups'],
              i['downs'],i['num_comments'],i['permalink'],i['selftext'],i['link_flair_text'],
              i['over_18'],i['thumbnail'],i['subreddit_id'],i['edited'],i['link_flair_css_class'],
              i['author_flair_css_class'],i['is_self'],i['name'],i['url'],i['distinguished']) for i in dr]
j = 0
dts = []
while j< len(to_db):
      dt = datetime.fromtimestamp(float(to_db[j][0]))
      #dts.append(dt.strftime("%Y-%m-%d %H:%M:%S"))
      #to_db[j][0] = dt.strftime("%Y-%m-%d %H:%M:%S")
      #print  dts
      j = j + 1
print to_db
cur.executemany("INSERT INTO crawlRD_redditcsv (created_utc, score,domain,tid,title,author,ups,downs,num_comments,permalink,"
                "selftext,link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,"
                "author_flair_css_class,is_self,name,url,distinguished)"
                 "VALUES (?, ?,?,?,?, ?,?,?,?, ?,?,?,?, ?,?, ?,?,?,?, ?,?,?);", to_db)
print i['created_utc']
print to_db[0][0], to_db[1][0],len(to_db)
con.commit()

