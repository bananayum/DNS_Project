import requests
import re
import os
import shutil
import threading
import time
import queue
import pymysql
import json
import ToSql

samplepre_pcap_dir = "C:/Users/lab130/Desktop/1/"#未分类样本路径
samplenex_pcap_dir = "C:/Users/lab130/Desktop/2/"#已分类样本路径


q=queue.Queue()
for filename in os.listdir(samplepre_pcap_dir):
    q.put(filename)


def spySample(fnm):
    while(True):
        try:
            filename=fnm.get()
            index = filename.rfind('.')
            sha256 = filename[:index]
            print(sha256)

            GET_URL = ("https://www.virustotal.com/ui/files/%s") % (sha256)

            proxyHost = "http-dyn.abuyun.com"
            proxyPort = "9020"
            proxyUser = "HA6HDP6X138R280D"
            proxyPass = "FF4F242106CA6538"
            proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                "host": proxyHost,
                "port": proxyPort,
                "user": proxyUser,
                "pass": proxyPass,
            }
            proxies = {
                "http": proxyMeta,
                "https": proxyMeta,
            }

            response = requests.get(GET_URL, proxies=proxies)
            if response.status_code==200:
                shutil.move(samplepre_pcap_dir + filename,samplenex_pcap_dir + filename)
            print(response.status_code)
            s = requests.session()
            s.keep_alive = False

            response_js=json.loads(response)
            virus_result=response_js["data"]["attributees"]["last_analysis_results"]
            family_result={}
            for key, value in virus_result.items():
                family_result[key]=value["result"]

            ToSql.run(sha256,family_result)

            time.sleep(1)
        except Exception as e:
            print(e)

# def toSql(family_result):
#     for i in family_result:
#         print(i)
#     sql = "INSERT INTO virusfamily({}) VALUES('%s')" % (i)
#     sqlfor = sql.format("aaa")
#
#     cursor.execute(sqlfor)
#     db.commit()

def start_thread():
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=spySample, args=(q,)))
    for thd in threads:

        time.sleep(0.5)
        thd.start()
    for thd in threads:
        thd.join()

if __name__ == '__main__':

    start_thread()

