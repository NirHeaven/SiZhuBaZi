# C_DiZhiCangGan = {
#     #
#     '寅': ('甲', '丙', '戊'),
#     '巳': ('丙', '庚', '戊'),
#     '申': ('庚', '壬', '戊'),
#     '亥': ('壬', '甲'),
#     #
#     '辰': ('戊', '乙', '癸'),
#     '未': ('己', '丁', '乙'),
#     '戌': ('戊', '辛', '丁'),
#     '丑': ('己', '癸', '辛'),
#     #
#     '卯': ('乙',),
#     '午': ('丁', '己'),
#     '酉': ('辛',),
#     '子': ('癸',),
# }

# C_WuXingDiZhi = {
#     '寅': ['木', 1],
#     '卯': ['木', 0],
#     '辰': ['土', 1],
#     '巳': ['火', 0],
#     '午': ['火', 1],
#     '未': ['土', 0],
#     '申': ['金', 1],
#     '酉': ['金', 0],
#     '戌': ['土', 1],
#     '亥': ['水', 0],
#     '子': ['水', 1],
#     '丑': ['土', 0],
# }

# qisha = {
#     '甲': '庚',
#     '乙': '辛',
#     '丙': '壬',
#     '丁': '癸',
#     '戊': '甲',
#     '己': '乙',
#     '庚': '丙',
#     '辛': '丁',
#     '壬': '戊',
#     '癸': '己',
# }
# DIZHI = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥',]
# C_YangTianGan = ['甲', '丙', '戊', '庚', '壬']
# C_YinTianGan = ['乙', '丁', '己', '辛', '癸']

# for i, tiangan  in enumerate(qisha, start=1):
#     for j, dizhi in enumerate(DIZHI, start=1):
#         if C_DiZhiCangGan[dizhi][0] == qisha[tiangan] and (i+j) % 2 == 0:
#             yiyang_tiangan = '阳' if tiangan in C_YangTianGan else '阴'
#             yiyang_dizhi = '阳' if C_WuXingDiZhi[dizhi][1] == 1 else '阴'
#             print(f'{tiangan}-{yiyang_tiangan}, {dizhi}-{yiyang_dizhi}, {C_DiZhiCangGan[dizhi]}')
from utils.analysis import getGanZhi
import sxtwl
print(getGanZhi(1993, 5, 13, 19, 0, '襄樊'))
print(sxtwl.getRunMonth(1994))
year = 1993
month = 3
day = 22
solar_date = sxtwl.fromLunar(year, month, day, True)
year, month, day = solar_date.getSolarYear(), solar_date.getSolarMonth(), solar_date.getSolarDay()
print(year, month, day)
lunar_date = sxtwl.fromSolar(year, month, day)
print(lunar_date.getLunarYear(), lunar_date.getLunarMonth(), lunar_date.getLunarDay())