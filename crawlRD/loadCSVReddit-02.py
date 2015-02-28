__author__ = 'Anne'
import csv, sqlite3
from datetime import datetime


def writeDB(fileName):
    allName = '../data/'+fileName
    with open(allName, 'rb') as csvfile:
         RedditReader = csv.DictReader(csvfile)
         RedditLine =[]
         for row in RedditReader:
             #print row['domain']
             if ( row['domain'].find('en.wikipedia.org')>-1 ):
                 RedditTime = datetime.fromtimestamp(float(row['created_utc'])).strftime("%Y-%m-%d %H:%M:%S")
                 RedditLine.append((RedditTime,row['score'],row['domain'],row['id'],row['title'],row['author'],row['ups'],
                    row['downs'],row['num_comments'],row['permalink'],row['selftext'],row['link_flair_text'],
                    row['over_18'],row['thumbnail'],row['subreddit_id'],row['edited'],row['link_flair_css_class'],
                    row['author_flair_css_class'],row['is_self'],row['name'],row['url'],row['distinguished'],fileName))
                 #print row['domain'],row['num_comments'],RedditTime
         print RedditLine


    cur.executemany("INSERT INTO crawlRD_reddit (created_utc, score,domain,tid,title,author,ups,downs,num_comments,permalink,"
                "selftext,link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,"
                "author_flair_css_class,is_self,name,url,distinguished,catName)"
                 "VALUES (?, ?,?,?,?, ?,?,?,?, ?,?,?,?, ?,?, ?,?,?,?, ?,?,?,?);", RedditLine)

    con.commit()


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
    #k=k+1
    #if (k<5):
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
        writeDB(row[2])


