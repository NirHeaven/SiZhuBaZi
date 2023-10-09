import requests
from bs4 import BeautifulSoup
import json
all_info = {}
rep = requests.get('http://mfsm.kvov.com/mfsmhelp.php')
soup = BeautifulSoup(rep.text, "lxml")
r = soup.find(attrs={'class': 'layui-table'})
for idx, item in enumerate(r.find_all('tr')):
    if idx == 0:
        continue
    t_data = []
    flag = True
    for i in item.find_all('td'):
        d = i.text
        if d == '':
            flag = False
            break
        t_data.append(d)
    if not flag:
        continue
    assert len(t_data) == 4
    print(t_data[1])
    assert t_data[1][0] in ['减', '加']
    if t_data[1][0] == '减':
        mul = -1
    else:
        mul = 1
    timeInfo = t_data[1][1:]
    hour, timeInfo = timeInfo.split('小时')
    minutes, timeInfo = timeInfo.split('分')
    seconds, timeInfo = timeInfo.split('秒')
    final_sec = int(seconds) + int(minutes) * 60 + int(hour) * 3600
    final_sec = final_sec * mul
    all_info[t_data[0]] = {'time':final_sec, 'longitude': float(t_data[2]), 'latitude': float(t_data[3])}
json.dump(all_info, open('真太阳时.json', 'w'), indent=2, ensure_ascii=False)
