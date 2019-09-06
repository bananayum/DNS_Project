import xml.etree.ElementTree as ET
import pymysql
import os

path='/Users/banana/Desktop/Heatwave2006/buildxml'

db=pymysql.connect("localhost","root","","",charset="UTF8")

for filename in os.listdir(path):
    print(filename)
    tree = ET.parse(path+'/'+filename)
    root = tree.getroot()
    print(root.tag)
    for pamrasterband in root:
        for meta in pamrasterband.findall('Metadata'):
            for mdi in meta.findall('MDI'):

                key=mdi.get('key')
                if key=='STATISTICS_MAXIMUM':
                    maximum=mdi.text

                if key=='STATISTICS_MINIMUM':
                    minimum=mdi.text

                if key=='STATISTICS_MEAN':
                    mean=mdi.text

                if key=='STATISTICS_STDDEV':
                    stddev=mdi.text

            cursor = db.cursor()
            sql = "INSERT INTO xmltype(FILENAME,STATISTICS_MAXIMUM,STATISTICS_MINIMUM,STATISTICS_MEAN,STATISTICS_STDDEV) " "VALUES('%s','%s','%s','%s','%s')" % (filename,maximum,minimum,mean,stddev)
            cursor.execute(sql)
            db.commit()

db.close()

