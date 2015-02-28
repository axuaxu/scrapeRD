__author__ = 'Anne'
import csv, sqlite3
from datetime import datetime


def writeDB(fileName):
    allName = '../data/'+fileName
    with open(allName,'rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    #created_utc,score,domain,id,title,author,ups,downs,num_comments,permalink,selftext,
    # link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,author_flair_css_class,
    # is_self,name,url,distinguished
        dr = csv.DictReader(fin) # comma is default delimiter
        tr = csv.reader(fin)
        to_db = [( datetime.fromtimestamp(float(i['created_utc']) ).strftime("%Y-%m-%d %H:%M:%S"),i['score'],i['domain'],i['id'],i['title'],i['author'],i['ups'],
              i['downs'],i['num_comments'],i['permalink'],i['selftext'],i['link_flair_text'],
              i['over_18'],i['thumbnail'],i['subreddit_id'],i['edited'],i['link_flair_css_class'],
              i['author_flair_css_class'],i['is_self'],i['name'],i['url'],i['distinguished'],fileName)  for i in dr]

    #print to_db
    #---
    j = 0
    dts = []
    to_reddit = []
    while j< len(to_db):
        #dt = datetime.fromtimestamp(float(to_db[j][0]))
        #dts.append(dt.strftime("%Y-%m-%d %H:%M:%S"))
         #to_db[j][0] = dt.strftime("%Y-%m-%d %H:%M:%S")
        dts = to_db[j][2]
        #print  dts
        if (dts.find('en.wikipedia.org')>-1):
            print 'find wikipedia',j,dts

            to_reddit.append([to_db[j][0],to_db[j][1],to_db[j][2],to_db[j][3],])
        else:
            #print 'no ',j,dts
            pass

        j = j + 1
    print to_reddit
    #---
    #cur.executemany("INSERT INTO crawlRD_redditcsvcat (created_utc, score,domain,tid,title,author,ups,downs,num_comments,permalink,"
    #            "selftext,link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,"
    #            "author_flair_css_class,is_self,name,url,distinguished,catName)"
    #             "VALUES (?, ?,?,?,?, ?,?,?,?, ?,?,?,?, ?,?, ?,?,?,?, ?,?,?,?);", to_db)

    #con.commit()


con = sqlite3.connect('..\db.csv')
con.text_factory = str
cur = con.cursor()

cur.execute("select * from crawlRD_redditsub where  load = 1")
all_rows = cur.fetchall()
k=0
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    #print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    #fileName = '../data/'+row[2]
    k=k+1
    if (k<15):
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
        writeDB(row[2])


