
C_WuXingShengL = ['木', '火', '土', '金', '水']
C_WuXingKeL = ['金', '木', '土', '水', '火']

C_WuXingSheng = {}
for i in range(len(C_WuXingShengL)):
    C_WuXingSheng[C_WuXingShengL[i]] = C_WuXingShengL[(i+1)%len(C_WuXingShengL)]

C_WuXingKe = {}
for i in range(len(C_WuXingKeL)):
    C_WuXingKe[C_WuXingKeL[i]] = C_WuXingKeL[(i+1)%len(C_WuXingKeL)]


C_WuXingSiShi = {
    '木': {'旺': '春', '相': '冬', '休': '夏', '囚': '季', '死': '秋'},
    '火': {'旺': '夏', '相': '春', '休': '季', '囚': '秋', '死': '冬'},
    '土': {'旺': '季', '相': '夏', '休': '秋', '囚': '冬', '死': '春'},
    '金': {'旺': '秋', '相': '季', '休': '冬', '囚': '春', '死': '夏'},
    '水': {'旺': '冬', '相': '秋', '休': '春', '囚': '夏', '死': '季'},
}