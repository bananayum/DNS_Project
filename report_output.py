import requests
import re
import os

SAMPLE_FILE = "malsimple.exe"
HEADERS = {"Authorization": "Bearer S4MPL3"}

# 查找任务id总数量
GET2_URL = "http://10.166.33.85:9000/cuckoo/status"
status_response = requests.get(GET2_URL)
found_txt = status_response.text
print(found_txt)
id_result = re.search('"reported":\s(\d+),.*?', found_txt)
idstr = id_result.group(1)
idnum = int(idstr) + 1

# 导出各项目的report文件，文件名为恶意样本名
for seq in range(1, 2):
    GET0_URL = ("http://10.166.33.85:9000/tasks/sample/%s") % (seq)
    GET1_URL = ("http://10.166.33.85:9000/tasks/report/%s") % (seq)

    tasksimple_response = requests.get(GET0_URL)
    name_target = tasksimple_response.text
    name_result = re.search('"target":\s.*?/.*?/.*?/.*?/(.*?)\..*?', name_target)
    temp_name = name_result.group(1)

    pcap_response = requests.get(GET1_URL)
    reportfile_name = ('/Users/banana/Desktop/恶意样本report/'+'%s' + '.json') % (temp_name)
    with open(reportfile_name, 'wb') as f:
        for reportchunk in pcap_response.iter_content(chunk_size=512):
            if reportchunk:
                f.write(reportchunk)