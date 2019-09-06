import requests
import re
import os
import shutil
import random

samplepre_pcap_dir = "/Users/banana/Desktop/未分类/恶意样本pcap"
samplenex_pcap_dir = "/Users/banana/Desktop/已分类/恶意样本pcap"


proxylist=[]
with open('ipproxy_tables') as proxyfile:
    for proxyline in proxyfile:
        proxyline = proxyline.strip('\n')
        proxylist.append(proxyline)

for filename in os.listdir(samplepre_pcap_dir):
    index = filename.rfind('.')
    sha256 = filename[:index]
    print(filename)
    proxy = random.choice(proxylist)
    print(proxy)
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    # GET_URL= "http://httpbin.org/get"
    GET_URL = ("https://www.virustotal.com/ui/files/%s")%(sha256)
    response = requests.get(GET_URL,proxies=proxies)
    sample_details = response.text
    print(sample_details)
    s = requests.session()
    s.keep_alive = False
    result = re.search('"names":.*?"(.*?)".*?', sample_details, re.S)
    sample_name_result=result.group(1)
    if sample_name_result=='.':
        sample_name_result='name_NULL'
    if sample_name_result == 'pe_info':
        sample_name_result = 'name_NULL'
    print(sample_name_result)
    i = 0
    for sample_filename in os.listdir(samplenex_pcap_dir):
        if sample_filename == sample_name_result:
            i = i + 1
        if i >= 1:
            break

    if i >= 1:
        shutil.move("/Users/banana/Desktop/未分类/恶意样本pcap/" + filename,
                    ("/Users/banana/Desktop/已分类/恶意样本pcap/%s/") % (sample_name_result) + filename)

    else:
        os.mkdir(("/Users/banana/Desktop/已分类/恶意样本pcap/%s/") % (sample_name_result))
        shutil.move("/Users/banana/Desktop/未分类/恶意样本pcap/" + filename,
                    ("/Users/banana/Desktop/已分类/恶意样本pcap/%s/") % (sample_name_result) + filename)
