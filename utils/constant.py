C_TianGan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
C_DiZhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
C_JQMC = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
C_WuXingShengL = ['木', '火', '土', '金', '水']
C_WuXingKeL = ['金', '木', '土', '水', '火']

C_ZHU = {
    0: '年',
    1: '月',
    2: '日',
    3: '时'
}

C_DayPerMonth  = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

C_WuXingSheng = {}
for i in range(len(C_WuXingShengL)):
    C_WuXingSheng[C_WuXingShengL[i]] = C_WuXingShengL[(i+1)%len(C_WuXingShengL)]

C_WuXingKe = {}
for i in range(len(C_WuXingKeL)):
    C_WuXingKe[C_WuXingKeL[i]] = C_WuXingKeL[(i+1)%len(C_WuXingKeL)]

C_WuXingTianGan = {}
for i in range(len(C_TianGan)):
    C_WuXingTianGan[C_TianGan[i]] = [C_WuXingShengL[i//2], 1 - i % 2]

# WuXingTianGan = {
#     '甲': ['木', 1],
#     '乙': ['木', 0],
#     '丙': ['火', 1],
#     '丁': ['火', 0],
#     '戊': ['土', 1],
#     '己': ['土', 0],
#     '庚': ['金', 1],
#     '辛': ['金', 0],
#     '壬': ['水', 1],
#     '癸': ['水', 0],
# }
C_WuXingDiZhi = {
    '寅': ['木', 1],
    '卯': ['木', 0],
    '辰': ['土', 1],
    '巳': ['火', 0],
    '午': ['火', 1],
    '未': ['土', 0],
    '申': ['金', 1],
    '酉': ['金', 0],
    '戌': ['土', 1],
    '亥': ['水', 0],
    '子': ['水', 1],
    '丑': ['土', 0],
}

C_TianGanWuHe = {
    ('甲', '己'): '合⋅化土',
    ('乙', '庚'): '合⋅化金',
    ('丙', '辛'): '合⋅化水',
    ('丁', '壬'): '合⋅化木',
    ('戊', '癸'): '合⋅化火',
}

C_TianGanSiChong = {
    ('甲', '庚'): None,
    ('乙', '辛'): None,
    ('丙', '壬'): None,
    ('丁', '癸'): None,
}

C_DiZhiLiuHe = {
    ('子', '丑'): '合⋅化土',
    ('寅', '亥'): '合⋅化木',
    ('卯', '戌'): '合⋅化火',
    ('辰', '酉'): '合⋅化金',
    ('巳', '申'): '合⋅化水',
    ('午', '未'): '',
}
C_DiZhiLiuChong = {
    ('子', '午'): None,
    ('丑', '未'): None,
    ('寅', '申'): None,
    ('卯', '酉'): None,
    ('辰', '戌'): None,
    ('巳', '亥'): None,
}
C_DiZhiLiuHai = {
    ('戌', '酉'): None,
    ('亥', '申'): None,
    ('子', '未'): None,
    ('丑', '午'): None,
    ('寅', '巳'): None,
    ('卯', '辰'): None,
}
C_DiZhiLiuPo = {
    ('子', '酉'): None,
    ('午', '卯'): None,
    ('申', '巳'): None,
    ('寅', '亥'): None,
    ('辰', '丑'): None,
    ('戌', '未'): None,
}
C_DiZhiSiXing = {
    #  无礼
    ('子', '卯'): None,
    ('卯', '卯'): None,
    # 恃势
    ('寅', '巳'): None,
    ('巳', '申'): None,
    ('申', '寅'): None,
    # 无恩
    ('丑', '戌'): None,
    ('戌', '未'): None,
    ('未', '丑'): None,
    # 自刑
    ('辰', '辰'): None,
    ('午', '午'): None,
    ('酉', '酉'): None,
    ('亥', '亥'): None,
}

C_DiZhiSiHuiFang = {
    ('寅', '卯', '辰'): '会⋅东方一气⋅木',
    ('巳', '午', '未'): '会⋅南方一气⋅火',
    ('申', '酉', '戌'): '会⋅西方一气⋅金',
    ('亥', '子', '丑'): '会⋅北方一气⋅水',
}
C_DiZhiWuHuiJu = {
    ('亥', '卯', '未'): '合木',
    ('寅', '午', '戌'): '合火',
    ('巳', '酉', '丑'): '合金',
    ('申', '子', '辰'): '合水',
    ('辰', '戌', '丑', '未'): '合土',
}
C_DiZhiBanHuiJu = {
    ('亥', '卯'): '半合木',
    ('卯', '未'): '半合木',
    ('寅', '午'): '半合火',
    ('午', '戌'): '半合火',
    ('巳', '酉'): '半合金',
    ('酉', '丑'): '半合金',
    ('申', '子'): '半合水',
    ('子', '辰'): '半合水',
}


C_DiZhiGong = {
    ('亥', '卯'): None,
    ('卯', '未'): None,
    ('亥', '未'): None,
    ('寅', '午'): None,
    ('午', '戌'): None,
    ('寅', '戌'): None,
    ('巳', '酉'): None,
    ('酉', '丑'): None,
    ('巳', '丑'): None,
    ('申', '子'): None,
    ('子', '辰'): None,
    ('申', '辰'): None,
}
C_DiZhiSiJi = {
    '春': ('寅', '卯', '辰'),
    '夏': ('巳', '午', '未'),
    '秋': ('申', '酉', '戌'),
    '冬': ('亥', '子', '丑'),
}
C_DiZhiCangGan = {
    '子': ('癸',),
    '丑': ('己', '癸', '辛'),
    '寅': ('甲', '丙', '戊'),
    '卯': ('乙',),
    '辰': ('戊', '乙', '癸'),
    '巳': ('丙', '庚', '戊'),
    '午': ('丁', '己'),
    '未': ('己', '丁', '乙'),
    '申': ('庚', '壬', '戊'),
    '酉': ('辛',),
    '戌': ('戊', '辛', '丁'),
    '亥': ('壬', '甲')

}

C_WuXingSiShi = {
    '木': {'旺': '春', '相': '冬', '休': '夏', '囚': '季', '死': '秋'},
    '火': {'旺': '夏', '相': '春', '休': '季', '囚': '秋', '死': '冬'},
    '土': {'旺': '季', '相': '夏', '休': '秋', '囚': '冬', '死': '春'},
    '金': {'旺': '秋', '相': '季', '休': '冬', '囚': '春', '死': '夏'},
    '水': {'旺': '冬', '相': '秋', '休': '春', '囚': '夏', '死': '季'},
}

C_ShiErChangSheng = {
    '甲': {'长生': '亥', '沐浴': '子', '冠带': '丑', '临官': '寅', '帝旺': '卯', '衰': '辰', '病': '巳', '死': '午', '墓': '未', '绝': '申', '胎': '酉', '养': '戌'},
    '乙': {'长生': '午', '沐浴': '巳', '冠带': '辰', '临官': '卯', '帝旺': '寅', '衰': '丑', '病': '子', '死': '亥', '墓': '戌', '绝': '酉', '胎': '申', '养': '未'},
    '丙': {'长生': '寅', '沐浴': '卯', '冠带': '辰', '临官': '巳', '帝旺': '午', '衰': '未', '病': '申', '死': '酉', '墓': '戌', '绝': '亥', '胎': '子', '养': '丑'},
    '丁': {'长生': '酉', '沐浴': '申', '冠带': '未', '临官': '午', '帝旺': '巳', '衰': '辰', '病': '卯', '死': '寅', '墓': '丑', '绝': '子', '胎': '亥', '养': '戌'},
    '戊': {'长生': '寅', '沐浴': '卯', '冠带': '辰', '临官': '巳', '帝旺': '午', '衰': '未', '病': '申', '死': '酉', '墓': '戌', '绝': '亥', '胎': '子', '养': '丑'},
    '己': {'长生': '酉', '沐浴': '申', '冠带': '未', '临官': '午', '帝旺': '巳', '衰': '辰', '病': '卯', '死': '寅', '墓': '丑', '绝': '子', '胎': '亥', '养': '戌'},
    '庚': {'长生': '巳', '沐浴': '午', '冠带': '未', '临官': '申', '帝旺': '酉', '衰': '戌', '病': '亥', '死': '子', '墓': '丑', '绝': '寅', '胎': '卯', '养': '辰'},
    '辛': {'长生': '子', '沐浴': '亥', '冠带': '戌', '临官': '酉', '帝旺': '申', '衰': '未', '病': '午', '死': '巳', '墓': '辰', '绝': '卯', '胎': '寅', '养': '丑'},
    '壬': {'长生': '申', '沐浴': '酉', '冠带': '戌', '临官': '亥', '帝旺': '子', '衰': '丑', '病': '寅', '死': '卯', '墓': '辰', '绝': '巳', '胎': '午', '养': '未'},
    '癸': {'长生': '卯', '沐浴': '寅', '冠带': '丑', '临官': '子', '帝旺': '亥', '衰': '戌', '病': '酉', '死': '申', '墓': '未', '绝': '午', '胎': '巳', '养': '辰'},
}

C_KongWangD = {
    '戌亥': ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉'],
    '申酉': ['甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛己', '壬午', '癸未'],
    '午未': ['甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳'],
    '辰巳': ['甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯'],
    '寅卯': ['甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑'],
    '子丑': ['甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥'],
}
C_KongWang = {}
for k in C_KongWangD:
    for v in C_KongWangD[k]:
        C_KongWang[v] = k


C_NaYinD = {
    '海中金': ['甲子', '乙丑'],
    '炉中火': ['丙寅', '丁卯'],
    '大林木': ['戊辰', '己巳'],
    '路旁土': ['庚午', '辛未'],
    '剑锋金': ['壬申', '癸酉'],
    '山头火': ['甲戌', '乙亥'],
    '涧下水': ['丙子', '丁丑'],
    '城头土': ['戊寅', '己卯'],
    '白蜡金': ['庚辰', '辛巳'],
    '杨柳木': ['壬午', '癸未'],
    '泉中水': ['甲申', '乙酉'],
    '屋上土': ['丙戌', '丁亥'],
    '霹雳火': ['戊子', '己丑'],
    '松柏木': ['庚寅', '辛卯'],
    '长流水': ['壬辰', '癸巳'],
    '沙中金': ['甲午', '乙未'],
    '山下火': ['丙申', '丁酉'],
    '平地木': ['戊戌', '己亥'],
    '壁上土': ['庚子', '辛丑'],
    '金箔金': ['壬寅', '癸卯'],
    '覆灯火': ['甲辰', '乙巳'],
    '天河水': ['丙午', '丁未'],
    '大驿土': ['戊申', '己酉'],
    '钗钏金': ['庚戌', '辛亥'],
    '桑柘木': ['壬子', '癸丑'],
    '大溪水': ['甲寅', '乙卯'],
    '沙中土': ['丙辰', '丁巳'],
    '天上火': ['戊午', '己未'],
    '石榴木': ['庚申', '辛酉'],
    '大海水': ['壬戌', '癸亥'],
}
C_NaYin = {}
for k in C_NaYinD:
    for v in C_NaYinD[k]:
        C_NaYin[v] = k


C_SanQi = {
    ('甲', '戊', '庚'): '天上三奇',
    ('乙', '丙', '丁'): '地上三奇',
    ('壬', '癸', '辛'): '人中三奇',
}

C_KuiGang = ['庚辰', '壬辰', '庚戌', '戊戌']
